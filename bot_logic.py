import random
import string

def gen_pass(pass_length):
    elements = string.ascii_letters + string.digits + "+-/*!$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)
    return password

def gen_emot():
    emot = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emot)

def coin():
    flip = random.randint(0, 1)  # Zmienione na 0-1 dla "Orzeł" i "Reszka"
    if flip == 0:
        return "Orzeł"
    else:
        return "Reszka"
