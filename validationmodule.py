

def validateNumber(num):
    if isinstance(num, int) or isinstance(num, float):
        return num
    return False

""" test cases """
if __name__ == '__main__':
    print(validateNumber(34))
    print(validateNumber(34.34))
    print(validateNumber("iti"))
    print(validateNumber(None))