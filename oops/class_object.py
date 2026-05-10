"""
In Python, a class object is the blueprint used to create objects (instances). 
It defines the properties (attributes) and behaviors (methods) that the objects created from it will have.

Simple explanation
A class = a template or blueprint
An object = a specific instance created from that class
"""

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(self.brand + " is driving")

"""Here:
Car is the class object
It defines:
attributes: brand, color
method: drive()
        """

car1 = Car("Toyota", "Red")
car2 = Car("BMW", "Black")

car1.drive()
car2.drive()