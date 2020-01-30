
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

# yell = shout


def person_does(name, func):
    return name + " says " + func("How hAs YoUr DAy beEN?")

message = person_does("nico", shout)
print(message)
message = person_does("nico", whisper)
print(message)
