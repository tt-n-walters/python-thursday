import requests
from datetime import datetime
from os import system

class ChatClient:
    def __init__(self, url, username):
        self.url = url
        self.username = username

    def send(self, message):
        if len(message) == 0:
            return
        if message.startswith("&"):
            exit()
        requests.post(self._get_send_url(), data={
            "name": self.username,
            "message": message,
            # "time": str(datetime.now().hour) + ":" + str(datetime.now().minute) + ":" + str(datetime.now().second),
            "time": "{:02}:{:02}:{:02}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
        })

    def receive(self):
        result = requests.get(self._get_receive_url())
        if result.status_code == 200:
            return result.text

    def _get_send_url(self):
        return self.url + "/send"
    
    def _get_receive_url(self):
        return self.url + "/messages"


chat = ChatClient("https://pythonavanzado.techtalents.cloud/chat", "Nico")

while True:
    text = input()
    chat.send(text)
    messages = chat.receive()
    # Split the one big string into individual messages.
    messages_split = messages.split("\n")
    # Select just the last 20 messages.
    messages_select = messages_split[-20:]
    # Join the messages back together, one on each line, and then print.
    system("cls")
    print("\n".join(messages_select))
