import requests

url = "https://pythonavanzado.techtalents.cloud/halloween"

response = requests.get(url + "/data")
random_data = response.text

print(random_data.find("h"))






# data = {
#     "name": "Nico",
#     "position": "something"
# }

# response = requests.get(url, params=data)

# if response.status_code == 200:
#     print(response.text)
