""" functions with mandatory number of arguments """
""" functions with known number of arguments  min// max"""
"1- define function"

def myfun():
    pass

# """to call function"""
# res=myfun()
# print(res) # None

"""2nd scenario"""

def sayhi():
    return

# res = sayhi()
# print(res)


"""3rd scenario"""
def sayHello():
    print("hello world")

# sayHello()

"""4th scenario"""

def getfullname():
    firstname= input("Enter your first name: ")
    lastname= input("Enter your last name: ")
    fullname= f"{firstname} {lastname}"
    return fullname

# fn = getfullname()
# print(fn)

"""5th scenario"""
def sumnum(num1, num2) : ## num1 , num2 --> arguments
    res = num1 + num2
    return res
# print(sumnum(3,4))

"""6th scenario"""

def multiply(num1, num2) :
    res = num1 * num2
    return res

# print(multiply(3,4))
# print(multiply(3))
#TypeError: multiply() missing 1 required positional argument: 'num2'  // runtime
# print(multiply(3,4,5))
# TypeError: multiply() takes 2 positional arguments but 3 were given


""" 7th scenario"""
""" functions with optional arguments """
def divnums(num1, num2=1):
    print(f"num1={num1}, num2={num2}")
    res = num1 / num2
    print(res)

# divnums(3)
#
# divnums(3,5)

# def divnums2(num1=3, num2):
#     print(f"num1={num1}, num2={num2}")
#     res = num1 / num2
#     print(res)
#
# # SyntaxError: non-default argument follows default argument

"""********************** functions with unknown number of arguments *******************************************"""
""" 8th scenario ---> """
""" function accept zero or more arguments 
* ==> zero or more 
"""
def analyze_offers(*offers):  # function accept zero or more arguemtns
    print(offers) # tuple ===>
    print("*************************************************")

# analyze_offers("VOIS")
# analyze_offers()
# analyze_offers("VOIS", "PWC")
# analyze_offers("GIZa-Systems","VOIS", "ITWORX")
#
# print("324", "234", "423434", 42343, "iti", sep = "|||", end="%%")
# print("jdkhgkj")

## one line==>

"""9th scenario --->"""

def introduceyourself(**info):
    print(info)  # dict
    print("**************************************")

# introduceyourself() ##
# introduceyourself(name='Ahmed', age= 24)  # key-word argument
# introduceyourself(fname='Mohamed', lname='ahmed', city='cairo')

""" ===== """



# def sumnums(num1, num2):  ## sum 2 numbers  ---> concat ??
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     print(res)
#     print("-------------------------------------")


# sumnums(2,4)
# sumnums("iti","python")


### validation
"""
    function sumnum(int num1 , int num2){
        res = num1 + num2
    }

"""

def sumnums(num1:int, num2:int) -> int:  #for documentation purpose
    print(f"num1={num1}, num2={num2}")
    res = num1 + num2
    print(res)
    print("-------------------------------------")


# sumnums(3,4)
# sumnums("iti", "abc")


""" We must do the validation manually ?  """
""" make sure that num1 and num2 are integers """

# print(type(3)==int)
#
# num1= 234
# print(type(num1)==int)
""" is instance -"""

print(isinstance("iti",str))
print(isinstance(33, float))



def sumnumss(num1:int, num2:int) -> int:  #for documentation purpose
    print(f"num1={num1}, num2={num2}")
    if isinstance(num1, int) and isinstance(num2, int):
        res = num1 + num2
        print(res)
        return res
    else:
        print("---Num1 and num2 must be integers ")
    print("-------------------------------------")

sumnumss(324,43)





