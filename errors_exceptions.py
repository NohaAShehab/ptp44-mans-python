"""

    try{}

    catch(){}

    else{}


    finally{}


"""

# try:
#     print(name)
# except :
#     print("--- problem happened")
# else:
#     pass
# finally:
#     pass
#
# print("000000000000000000000000")
"""  """

# try:
#     num= 10
#     print(num/0)
# except :
#     print("--- problem happened")
# else:
#     pass
# finally:
#     pass
#
# print("000000000000000000000000")

""" exception types """
# try:
#     # num= 10
#     print(num/0)
# except Exception as e  :
#     print(f"--- problem happened {e}")
# else:
#     pass
# finally:
#     pass
#
# print("000000000000000000000000")


""" try --> more than one except """


# try:
#     num= 10
#     res = num/0
# ## except block is called when problem happend
# except NameError as ne :
#     print(f"--- name not found {ne}")
#     num = 0
# except ZeroDivisionError as ze:
#     print(f"--- zero {ze}")
#     res = 0
# except Exception as e  :
#     print(f"--- problem happened {e}")
# else:
#     pass
# finally:
    # pass

# print("000000000000000000000000")

""" else block """
# try:
#     num = int(input("Enter a number: "))
# except Exception as e:
#     print(e)
#
# num = num* 10
# print(num)

# try:
#     num = int(input("Enter a number: "))
# except Exception as e:
#     print(e)
# else:
#     print("--- will be executed if there are no problems")
#     num = num* 10
#     print(num)
#
#

"""finally"""
# try:
#     num = int(input("Enter a number: "))
# except Exception as e:
#     print(e)
# else:
#     print("--- will be executed if there are no problems")
#     num = num* 10
#     print(num)
#
# finally:
#     "is exectued always "
#     print("--- process is finished ")
#
# print("===== bye bye ")
""" ---------------------> """
# try:
#     num = int(input("Enter a number: "))
# except ZeroDivisionError as e:
#     print(e)
# else:
#     print("--- will be executed if there are no problems")
#     num = num* 10
#     print(num)
#
# finally:
#     "is exectued always "
#     print("--- process is finished ")
#
# print("===== bye bye ")






""" """

def askforInt():
    try:
        num = int(input("please enter an integer: "))
    except Exception as e:
        print(e)
        return  False
    else:
        return num
    print("------------------------")

# print(askforInt())

def askforIntt():
    try:
        num = int(input("please enter an integer: "))
    except Exception as e:
        print(e)
        return  False
    else:
        print("--- returning with value")
        return num
    finally:
        # priorty of executing finally block in try expression
        # used in function preceeds return
        print("-----------the process completed finally-------------")

# print(askforIntt())
# print("---**************************************")
#
# print(askforIntt())


def askforInttt():
    try:
        num = int(input("please enter an integer: "))
    except Exception as e:
        print(e)
        return  False
    else:
        print("--- returning with value")
        return num
    finally:
        # priorty of executing finally block in try expression
        # used in function preceeds return
        print("-----------the process completed finally-------------")
        return "bye"

print(askforInttt())
print("---**************************************")

print(askforInttt())









