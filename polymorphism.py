""" no explict overloading in python

    ---> overcome  ==> default arguments


    ---> overlaoding  --> external lib --> overload


    https://pypi.org/project/overloading/

"""

class Person:
    def __init__(self, name):
        self.name = name

    def printPerson(self):
        print(f"My name is {self.name}")



class Engineer(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

    def printPerson(self):
        super().printPerson()
        print(f"My email is {self.email}")


eng= Engineer("df", "fsjdf")
eng.printPerson()








