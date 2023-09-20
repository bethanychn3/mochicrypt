# file for any functions created
from hashlib import sha256

def make_hash(new_str:str) -> hash:
    """Generates a hash from a given string value,
    
    Arg:
        new_str: A newly inputed password/code by the user.
        
    Returns: 
        A hash value. 
    """
    h = sha256()
    new_str2 = new_str.strip()
    h.update(new_str2.encode())
    hash_value = h.hexdigest()
    return hash_value

def read_file() -> None:
    """Opens a file to be read."""

    f = open("SAVED.txt", "r")
    return f

def remake_string(split_line:list) -> str:
    """Puts the rest of the line together after being split.
    
    Arg:
        split_line: A list of strings.

    Returns:
        A string.
    """
    new_str = ""
    split_line = split_line[1:]
    for word in split_line:
        new_str += f" {word}"
    return new_str

def verify_pass(file, new_pass:str) -> str:
    """Verifies that the access code exists and finds and returns corresponding value.

    Args:  
        file: An opened file.
        new_pass: A new user input access code.
    
    Returns:
        A string of either denial or the accessed string.
    """
    hash_val = make_hash(new_pass)
    for line in file:
        l = line.split(" ")
        if l[0] == hash_val:
            return remake_string(l)
    return "NOT FOUND"

#fi = read_file()
#print(verify_key(fi, "adf"))

def write_file(hash_key:hash, info:str) -> None:
    """Opens the File and stores the info.

    Args:
        hash_key: The hash value of the access code;
        info: The secret string to be stored.
    """
    file = open("SAVED.txt", "a")
    line = f"{hash_key} {info}\n"
    file.write(line)
    file.close()

#write_file("abc", "test")

def check_capacity() -> str:
    """Checks if the capcacity of the file has been reached.
    
    Returns:
        A string.
    """
    file = read_file()
    count = 0
    for l in file:
        count += 1
    if count >= 20:
        return "full"
    return "available"

#-------UNUSED-----------
# def make_key() -> str:
#     selection = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*_-?<>+"
#     new_key = ""
#     count = 0
#     while count < 9:
#         new_key += random.choice(selection)
#         count += 1
#     return new_key