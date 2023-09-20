# main program that runs mochicrypt
import f

def store_secret() -> None:
    """Stores the user's inputed data into the file."""
    
    data = input("Please Enter The information You Would Like to Encrypt: ")
    password = input("Please Enter an Access Code: ")
    new_hash = f.make_hash(password)
    f.write_file(new_hash, data)

def find_secret() -> None:
    """Finds the corresponding information to the entered password/code."""

    user_pass = input("Please enter your access code: ")
    file_open = f.read_file()
    verification = f.verify_pass(file_open, user_pass)
    if verification == "NOT FOUND":
        print("Sorry, the password does not match with any stored information in the database.")
    else:
        print(f"Your Secret: {verification}")

def run_processes():
    """Runs the different options presented to the user."""

    print("Here's a List of Available Options: ")
    print("[1] Store Data \n[2] Find Data\n")
    picked = input("Please input the corresponding number of your selected option: ")
    while (picked != "1") and (picked != "2"):
        picked = input("Please input the corresponding number of your selected option: ")
    if picked == "1":
        store_secret()
    else:
        find_secret()

def main():
    """The Main Process."""

    print("MOCHICRYPT AN UNOFFICIAL ENCRYPTION AND STORAGE :)")
    print("--------------------------------------------------\n")
    if f.check_capacity() == "full":
        print("Sorry, Mochicrypt is at MAX CAPACITY.")
        return
    else:
        run_processes()
        print("Thank you!")

main()

#--------UNUSED-------------
# def generate_key():
#     flag = False
#     while flag is False:
#         new_key = f.make_key()
#         file = f.read_file()
#         if f.verify_key(file, new_key):
#             flag = True
#             return new_key