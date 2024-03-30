

""" import another module """

# import modules_packages
#
# print(modules_packages.name)
# modules_packages.sayWelcome()

""" alias module"""
# import modules_packages as mymodule
# print(mymodule.name)

""" import part of the module """
# from modules_packages import name, sayWelcome

""" alias functioname"""
# from modules_packages import  sayWelcome as myfun

############################################################################

""" check this """
import modules_packages




""" each module in python has its own main
    __name__ == "__main__"

"""

from validationmodule import validateNumber
def sumnum(num1 , num2):
    if validateNumber(num1) and validateNumber(num2):
        return num1 + num2
    return None

print(sumnum(4,35))









