import random
import string
import math


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


print("Generated password:", generate_password())
print("Square root of 64:", math.sqrt(64))
