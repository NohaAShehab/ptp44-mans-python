"""

    class Person{
        public $name;
        private $salary;

        function setSalary($sal){


        }

    }


"""
""" Access modifiers --> public, protected , private """

""" 1----- No  ACCESS MODIFIERS in PYTHON

    python use naming convention to represent access modifiers 
    
    property/function 
    a->zA-Z  ---> public 
    _ ----> protected 
    __ =---> private 

"""
# class Employee:
#     def __init__(self, name, email,salary):
#         self.name = name
#         self._email = email
#         self.__salary = salary
#
#
# emp = Employee("Mohamed", "moha@gmail.com", 100000)

# print(emp.name)
# emp.name = 'Mohamed Ismail'
# print(emp._email)  # Ethically Don't do this
# # print(emp.__salary)
# print(emp.__dict__)
# print(emp._Employee__salary) # # Ethically Don't do this
#
# emp._Employee__salary = "updated"


""" setters and getters """



# class Employee:
#     def __init__(self, name, email,salary):
#         self.name = name
#         self._email = email
#         self.__salary = salary
#
#     def getSalary(self):
#         return self.__salary
#
#     def setSalary(self, sal):
#         if isinstance(sal, int) or isinstance(sal, float) and sal> 0:
#             self.__salary = sal
#         else:
#             raise ValueError("Invalid salary, salary must be number greater than zero")
#
# emp = Employee("Mohamed", "moha@gmail.com", 100000)
# print(emp.getSalary())
# # emp.setSalary('djsjkfh')
# emp.setSalary(8923672356)
""" use property decorator """

# class Employee:
#     def __init__(self, name, email,salary):
#         self.name = name
#         self._email = email
#         self.__salary = salary
#
#     @property
#     def salary(self):
#         return self.__salary
#
#
#     @salary.setter
#     def salary(self, sal):
#         if isinstance(sal, int) or isinstance(sal, float) and sal> 0:
#             self.__salary = sal
#         else:
#             raise ValueError("Invalid salary, salary must be number greater than zero")
#
#
#     def getSalary(self):
#         return self.__salary
#
#     def setSalary(self, sal):
#         if isinstance(sal, int) or isinstance(sal, float) and sal> 0:
#             self.__salary = sal
#         else:
#             raise ValueError("Invalid salary, salary must be number greater than zero")
#
# emp = Employee("Mohamed", "moha@gmail.com", 100000)
# print(emp.salary)  # visualize object -->
# print(emp.__dict__)
#
# emp.salary = "iti"
# print("-------")


""" more organized"""
# class Employee:
#     def __init__(self, name, email,salary):
#         self.name = name
#         self._email = email
#         # self.__salary = salary
#         if isinstance(salary, int) or isinstance(salary, float) and salary > 0:
#             self.__salary = salary
#         else:
#             raise ValueError("Invalid salary, salary must be number greater than zero")
#
#     @property
#     def salary(self):
#         return self.__salary
#
#
#     @salary.setter
#     def salary(self, sal):
#         if isinstance(sal, int) or isinstance(sal, float) and sal> 0:
#             self.__salary = sal
#         else:
#             raise ValueError("Invalid salary, salary must be number greater than zero")
#
#
#
# emp = Employee("Mohamed", "moha@gmail.com", "iti")
# print(emp)
# print(emp.salary)
# # print(emp.salary)  # visualize object -->
# # print(emp.__dict__)
# #
# # emp.salary = "iti"
# # print("-------")
#
#
#
#
#


""" """
class Employee:
    def __init__(self, name, email,salary, byear):
        self.name = name
        self._email = email
        self.salary = salary
        self.byear = byear

    @property
    def age(self):
        return 2024-self.byear
    @property
    def salary(self):
        return self.__salary


    @salary.setter
    def salary(self, sal):
        if isinstance(sal, int) or isinstance(sal, float) and sal> 0:
            self.__salary = sal
        else:
            raise ValueError("Invalid salary, salary must be number greater than zero")



emp = Employee("Mohamed", "moha@gmail.com", 897876, 1992)
print(emp)
print(emp.salary)

print(emp.age)
emp.age = 27






















