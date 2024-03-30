

# def sumnum(num1 , num2 ):
#     print(f"num1={num1}, num2={num2}")
#     if isinstance(num1, int) and isinstance(num2, int):
#         return num1 + num2
#
#     raise TypeError("Num1 and num2 must be integers")
#
# print(sumnum("ITI","PTTHON"))


def divnums(num1, num2):
    if num2==0:
        raise ZeroDivisionError("num2 cannot be zero")
    print(f"num1={num1}, num2={num2}")
    res  =num1/ num2
    print(res)


divnums(4,0)









