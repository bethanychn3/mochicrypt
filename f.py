# file for any functions created
import random
#import o

# def make_key() -> str:
#     selection = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*_-?<>+"
#     new_key = ""
#     count = 0
#     while count < 9:
#         new_key += random.choice(selection)
#         count += 1
#     return new_key
def make_hash(new_str):
    new_str2 = new_str.strip()
    hash_value = hash(new_str2)
    return hash_value

def read_file():
    f = open("SAVED.txt", "r")
    return f

def verify_pass(file, new_pass) -> str:
    hash_val = new_pass.strip()
    new_hash = hash(hash_val)
    print(new_hash)
    for line in file:
        l = line.split(" ")
        print(l[0])
        if l[0] == new_hash:
            return l[1]
    #print(hash("password"))
    #print(hash("password"))
    return "NOT FOUND"

#fi = read_file()
#print(verify_key(fi, "adf"))

def write_file(hash_key, info):
    file = open("SAVED.txt", "a")
    line = f"{hash_key} {info}\n"
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

# write a hash function and store hash in the document
# if the hashes of the password entered matches the one stored, then the information can be seen

