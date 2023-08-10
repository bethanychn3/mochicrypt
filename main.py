# main program that runs mochicrypt
import f
#import o

def generate_key():
    flag = False
    while flag is False:
        new_key = f.make_key()
        file = f.read_file()
        if f.verify_key(file, new_key):
            flag = True
            return new_key


def main():
    print("MOCHICRYPT AN UNOFFICIAL ENCRYPTION AND STORAGE :)")
    print("--------------------------------------------------\n")
    if f.check_capacity() == "full":
        print("Sorry, Mochicrypt is at MAX CAPACITY.")
        return
    else:
        data = input("Please Enter The information You Would Like to Encrypt: ")
        key = generate_key()
        f.write_file(key, data)
        print(f"YOUR NEW KEY IS {key}")
        print("Thank you!")

    #print("hello world")

main()
