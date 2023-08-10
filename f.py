# file for any functions created
import random
#import o

def make_key() -> str:
    selection = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*_-?<>+"
    new_key = ""
    count = 0
    while count < 9:
        new_key += random.choice(selection)
        count += 1
    return new_key

def read_file():
    f = open("SAVED.txt", "r")
    return f

def verify_key(file, new_key) -> bool:
    for line in file:
        l = line.split(" ")
        #print(l[0])
        if l[0] == new_key:
            return False
    return True

#fi = read_file()
#print(verify_key(fi, "adf"))

def write_file(key, info):
    file = open("SAVED.txt", "a")
    line = key + " " + info + "\n"
    file.write(line)
    file.close()

#write_file("abc", "test")

def check_capacity():
    file = read_file()
    count = 0
    for l in file:
        count += 1
    if count >= 20:
        return "full"
    return "available"
