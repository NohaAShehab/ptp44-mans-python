

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