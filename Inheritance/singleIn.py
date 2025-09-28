#Multi level Inheritance
class Car:
  @staticmethod
  def start():
    print("car started..")

  @staticmethod
  def stop():
    print("car stopped..")

class ToyotaCar(Car):
  def __init__(self, brand):
    self.singh = brand
  

class Fortuner(ToyotaCar):
  def __init__(self, type):
    self.type = type

car1.type="Disel"
car1.stop()
print(car1.type)
car1.singh