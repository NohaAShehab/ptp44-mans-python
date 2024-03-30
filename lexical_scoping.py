name ='Ahmed'  # global variable
""" this varaible can be accessed anywhere in the script """


def printCourse():
    course=  "python"   # local variable --> variable can be accessed only
    # from inside function
    print(f"===course: {course}")


# printCourse()
# print(course)
# print(name)

""" access global variables  from inside the function """
coursename = 'python'
def printCourseName():
    # print global variable from inside the function
    print(f"from inside the function coursename= {coursename}")

# printCourseName()

""
# def modifyCourseName():
#     coursename= 'django'  # new  local variable inside the function
#     print(f"from inside the function coursename= {coursename}")
#
# modifyCourseName()
# print(coursename)
""" I need to modify global variable from inside the function """
# coursename = 'python'
# def modifyCourseName():
#     global coursename  # please don't create new local variable
#     coursename= 'django'  #  use the global variable
#     print(f"from inside the function coursename= {coursename}")
#
# modifyCourseName()
# print(coursename)



""" check this scenario """


# def outerfunction():
#     salary = 287923
#     def printSalary():
#         # access local variable from inside the inner function
#         print(f"My salary ={salary}")
#
#     printSalary()
#
#     print(f"salary= {salary}")
#
# outerfunction()

"""    """
# def outerfunction():
#     salary = 287923  # new local variable for the outer
#     def printSalary():
#         # access local variable from inside the inner function
#         print(f"My salary ={salary}")
#
#     printSalary()
#
#     def modifySalary():
#         salary = 1000000 # new local variable for the inner function
#         print(f"modified salary={salary}")
#     modifySalary()
#
#     print(f"salary= {salary}")
#
# outerfunction()





















def outerfunction():
    salary = 287923  # new local variable for the outer
    def printSalary():
        # access local variable from inside the inner function
        print(f"My salary ={salary}")

    printSalary()

    """ modify local variable from  inner function"""
    """ I need to use the local variable of the parent """
    def modifySalary():
        nonlocal salary  # plz don't create the local variable , use the parent local one
        salary = 1000000
        print(f"modified salary={salary}")
    modifySalary()

    print(f"salary= {salary}")

outerfunction()







