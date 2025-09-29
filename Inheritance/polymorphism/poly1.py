# print(1 + 3)
# print("Himanshu" + "singh") # concatenate
# print[1, 2, 3] + [4, 5, 6] # its merge the list

#complex number
"""
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +",self.img,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(2, 4)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()  """


## Practice question
"""
class Circle:
    def __init__(self, radius):
        self.r = radius
    def area(self):
        return (22/7) * self.r ** 2

    def perimeter(self):
        return 2 * (22/7) * self.r

c1 = Circle(21)
print(c1.area())
print(c1.perimeter()) """

# Define a Employee class with attribbute role, department & salary
"""
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("department =", self.department)
        print("salary =", self.salary)

# e1 = Employee("accountant", "Finance", "6000.00")
# e1.showDetails()

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75000.00")

engg1 = Engineer("Elon Musk", 40)
engg1.showDetails()   """

# Create a class called order which stores item & its price
#use Dunder function __gt__() to convey that:
# order1> order2 if price of order1> price of order2
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):  #Dunder Function
        return self.price > ord2.price


ord1 = Order("chips", 20)
ord2 = Order("tea", 45)
print(ord1 >ord2)
