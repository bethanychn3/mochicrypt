# file for any functions created
import random

def key_maker() -> str:
    selection = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*_-?<>+"
    new_key = ""
    count = 0
    while count < 9:
        new_key += random.choice(selection)
        count += 1
    return new_key
