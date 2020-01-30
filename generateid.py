# py.__module__
import random
import string

def generate_id(length):
    # List all the possible choices of letter/number
    possibles = string.ascii_letters + string.digits + "-_"
    # Start off our random id with nothing.
    id = ""
    
    # Loop to choose multiple random letters/numbers.
    for i in range(length):
        # Choose a random letter from the possible letters/numbers.
        random_letter = random.choice(possibles)
        # Add the random letter/number to the random id.
        id = id + random_letter

    return id

if __name__ == "__main__":
    raise RuntimeError("You have run a file that must be imported!")
