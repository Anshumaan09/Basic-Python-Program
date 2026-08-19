class car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

cars = car("blue", "mercedes")
print(cars.color, cars.brand)

# Constructor
# __init__ is used as constructor
# It invokes during object creation

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def greeting(self):
        print("Hello",self.name)
    
    def marking(self):
        return self.marks

S1 = Student("Anshumaan", 100)
print(S1.greeting())
print(S1.marking())

# __ -> makes it private
# we have to call it internally to access it
class Person:
    __name = "anonyomous"
    
    def __hello(self):
        print("hello person!")
        
    def welcome(self):
        self.__hello()
    
p1 = Person()
# print(p1.__name)
print(p1.welcome())

