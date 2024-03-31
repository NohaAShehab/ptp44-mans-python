
# class Person:
#     pass
#
# class Engineer(Person):
#     pass
#
# """ inheritance  ---> is a --> relationhsip"""
#
# eng = Engineer()
# print(isinstance(eng, Person))

"""2nd scenario """
# class Person:
#     def __init__(self, name):
#         self.name = name
#
# class Engineer(Person):
#     pass
#
# """ inheritance  ---> is a --> relationhsip"""
#
# eng = Engineer("noha")
# print(isinstance(eng, Person))

"""3rd scenario"""
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def displayname(self):
#         print(f"name = {self.name}")
#
# class Engineer(Person):
#     def __init__(self,name, salary):
#
#         # call parent constructor
#         super().__init__(name)
#         # customize object
#         self.salary = salary
#
# """ inheritance  ---> is a --> relationhsip"""
#
# eng = Engineer("noha", 482947)
# print(isinstance(eng, Person))
# eng.displayname()

""" python multiple inheritance"""

# class A():
#     pass
#
# class B():
#     pass
#
# class Child(A, B):
#     pass




"""2nd scenario"""


# class A():
#     pass
#
# class B():
#     def __init__(self):
#         print("B object is being created ")
#
# class Child(A, B):
#     pass
#
#
# childd = Child()


""" """

# class A():
#     def __init__(self):
#         print('A object is being created ')
#
# class B():
#     def __init__(self):
#         print("B object is being created ")
#
# class Child(A, B):
#     pass
#
#
# childd = Child()


""" before final scenario"""

# class Basic:
#     def __init__(self):
#         print("Basic is being created ")
#
# class A(Basic):
#     def __init__(self):
#         print('A object is being created ')
#
# class B(Basic):
#     def __init__(self):
#         print("B object is being created ")
#
# class Child(A, B):
#     pass


# childd = Child()

""" final scenario"""
# class Basic:
#     def __init__(self):
#         print("Basic is being created ")
#
# class A(Basic):
#     def __init__(self):
#         super().__init__()
#         print('A object is being created ')
#
# class B(Basic):
#     def __init__(self):
#         print("B object is being created ")
#
# class Child(A, B):
#     pass
#
#
# childd =Child()




""" final scenario"""
class Basic:
    def __init__(self):
        print("Basic is being created ")

class A(Basic):
    def __init__(self):
        super().__init__()
        print('A object is being created ')

class B(Basic):
    def __init__(self):
        super().__init__()
        print("B object is being created ")

class Child(A, B):
    pass


childd =Child()






































