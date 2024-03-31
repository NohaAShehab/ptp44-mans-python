# emp  = {
#     "firstName": "Ahmed",
#     "lastName": "Ali",
#     "salary": 5000
# }
#
# emp2 = {
#     "fname" : "Ali",
#     "sal": 34534,
#     "lname": "Mohamed"
#
# }

def printEmp(emp:dict):
    print(f"{emp['firstName']}, {emp['lastName']}")

# printEmp(emp)
# printEmp(emp2)

""" create ower own datatype --> create class """

"""1- define a class """

# class Employee:
#     pass

"""2- take an object from the class """
# emp = Employee()
# print(emp, type(emp))
# name = 'ahmed'
# print(name, type(name))
# emp.name = 'Ahmed'
# emp.salary= 78462
#
#
# emp2= Employee()
# emp2.fname = 'ahmed'
# emp2.lname = 'Ali'

"""3- customize object creation"""
# class Employee:
#     """constructor in python"""
#     def __init__(self):
#         """allocate place to the object in memory """
#         print("object is being created")
#         print(self)
#         # name , email , salary ---> instance variable
#         self.name = 'ahmed'
#         self.email='ahmed@gmail.com'
#         self.salary = 232435


#
# emp = Employee()
# print("****************************")
# emp2 = Employee()



"""customize """

# class Employee:
#     """constructor in python"""
#     def __init__(self,name, email , salary):
#         # name , email , salary ---> instance variable
#         self.name = name
#         self.email=email
#         self.salary = salary
#
# emp= Employee("ahmed", "a", 91208)
# emp2 =  Employee("abc", "abc", 9238394)

"""operation on object // instance """
# class Employee:
#     """constructor in python"""
#     def __init__(self,name, email , salary):
#         # name , email , salary ---> instance variable
#         self.name = name
#         self.email=email
#         self.salary = salary
#
#     """instance method ---> first argument in method ---> object address--> self"""
#     # def printEmp(abbass):
#     #     print(abbass)
#     def printEmp(self):
#         print(f'{self.name}, {self.email}, {self.salary}')
#
# emp= Employee("ahmed", "a", 91208)
# emp2 =  Employee("abc", "abc", 9238394)
#
# emp.printEmp()

"""count no of objects taken from class 
define property represent class itself --> not object 
"""
# class Employee:
#     count = 0  # class variable
#     """constructor in python"""
#     def __init__(self,name, email , salary):
#         self.name = name
#         self.email=email
#         self.salary = salary
#         # Employee.count+=
#         print(self.__class__)
#         self.__class__.count +=1
#         self.id = Employee.count
#
#     def printEmp(self):
#         print(f'{self.name}, {self.email}, {self.salary}')


# "1- access class variable using className"
# print(Employee.count)
# # Employee.count = 10
#
# emp= Employee("ahmed", "a", 91208)
# emp2 =  Employee("abc", "abc", 9238394)
#
# """display object properties inform of dict """
# print(emp.__dict__)
#
# emp.printEmp()

""" define behaviour represent class """

class Employee:
    count = 0  # class variable
    """constructor in python"""
    def __init__(self,name="", email="" , salary=""):
        self.name = name
        self.email=email
        self.salary = salary
        self.__class__.count +=1
        self.id = Employee.count

    def printEmp(self):
        print(f'{self.name}, {self.email}, {self.salary}')

    @classmethod  # decorator --> change function behaviour
    def classfun(cls):
        print(cls)
        print(f"total number of employees: {cls.count}")
        pass


    # class method ---> object factory create default object
    @classmethod
    def create_emp(cls):
        return cls("default", "defaut", 8968)

    def create_employee(self):
        return self.__class__("Ahmed", "ddf", 3891274)

""" class method ? --> call method using class"""
Employee.classfun()
Employee.city='Cairo' # class variable --> shared property between all instances in the class

emp2= Employee("Ahmed", "ddf", 3891274)
emp3 = Employee.create_emp()



"""

    class Complexx:
        pass
        
    c  = Complexx()
    c2 = Complexx()
    
    add 
    # c3 = c.addobject(c2) 
    c3= Complexx.add(c, c2)
    
    
    ====> 
    c = c + c2 
    c.addobject(c2) ## modify in the same object 
    
    --> special mehtod 
    __add__ ---> + operator


"""

""" All class in python extends// inherits from base class object """


# class Person:
#     pass
#
# p = Person()
#
# print(isinstance(p , Person))
# print(isinstance(p, object))
# print(isinstance("iti", object))
#






""" ----> check this """
class Employee:

    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary

    @staticmethod  # represent helper method // doesn't depend on class// instance
    def cal_net_salary(salary):  # helper function
        return salary * .8



emp = Employee("jksfh", "ks962", 9082)


"""use static method """

print(Employee.cal_net_salary(236548236478246))
print(Employee.cal_net_salary(emp.salary))
# def cal_net_salary(salary):  # helper function
#     return salary*.8
#
# print(cal_net_salary(emp.salary))
#
# print(cal_net_salary(200000))















