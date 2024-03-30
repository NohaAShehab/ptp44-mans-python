

""" any .py file is considered to be python module """
print("---- welcome to the best python module you will ever use ")
name = 'ahmed'

def sayWelcome():
    guestname = input("What is your name? ")
    print(f"Welcome {guestname} to python course. ")

## restrict that somelines will be executed unless the called from this file / module
if __name__ == "__main__":
    print(name)
    sayWelcome()