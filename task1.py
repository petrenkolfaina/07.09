class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname= surname
        self.age = age

    def showInfo(self):
        print(f"Name: {self.name}, surname: {self.surname}, age:{self.age}")

name = input("Enter your name")
surname = input("Enter your surname")
age = input("Enter your age")

obj1 = Person(name, surname, age)

obj1.showInfo()