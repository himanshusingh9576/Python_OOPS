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
print(car1.type)