"""
#Multiple Inheritance
class A:
    varA = "welcome to class A"
class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()
print(c1.varA)"""


## SUPER() METHOD
"""
class Car:
    def __init__(self, type):
        self.type = type
    
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()
        super().stop()

car1 = ToyotaCar("prius", "electric")
print(car1.type)  """


# Class Method
"""
class Person:
    name = "anonymous"

    # def changeName(self, name):
    #     self.singh = name
    #     # Person.name = name
    #     self.__class__.name = "Rahul" # instance method

    @classmethod
    def changeName(cls, name):
        cls.singh = name
        cls.name = name

p1 = Person()
p1.changeName("rahul")
print(p1.singh)
print(Person.name) """


# Property decoraator
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        

    # def calcPercentage(self):
    #     self.percentage = str((self.phy + self.math + self.chem)/3) + " %"
    @property
    def percentage(self) :
        return str((self.phy + self.math + self.chem)/3) + " %"

stu1 = Student(99, 98, 97)
print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)
print(stu1.phy)