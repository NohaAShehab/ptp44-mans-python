

def askforInt(message="input please enter number: "):
    while True:
        num = input(message)  # string
        if num.isdigit():
            return int(num)
        print("--- please enter valid number --- ")


if __name__ == "__main__":
    print(askforInt("Please enter age "))