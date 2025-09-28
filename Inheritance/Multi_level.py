# Multi-level Inheritance

class Car:
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stoped..")

class ToyotaCar(Car):
    def __init__(self, name):
        self.singh = name

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("Disel")
print(car1.type)
car1.start()
