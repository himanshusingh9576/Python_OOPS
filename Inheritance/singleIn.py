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
  
car1 = ToyotaCar("disel")


car1.stop()

