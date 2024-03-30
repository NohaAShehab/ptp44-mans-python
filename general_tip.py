

# for i in range(1,4):
#     password = input(f"please enter password:{i}: ")
#     if password=='123':
#         print("--- logged successfully ---")
#         break
#
# if i==3 and password!="123":
#     print("account has been locked ")



""" for else ? """


for i in range(1,4):
    password = input(f"please enter password:{i}: ")
    if password=='123':
        print("--- logged successfully ---")
        break
else:
    """ if the loop completed without been broken """
    print("account has been locked ")
print(f"i= {i}")

for i in range(10 , 1 , -1):
    print(i)

"""
myfun(5, 4)
-->(4,5,6,7,8)

'abdulrahman'
    abdu
    lr
    ahm
    an 
    
    
    ["apple","banana","cherry","kiwi", "iti"]
    noha 
    -----
    enter char m
    -----
    enter char : p
    -pp--
    
"""