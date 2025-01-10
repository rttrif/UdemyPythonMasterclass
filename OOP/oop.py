"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.

self - is the reference on this class.

"""


class Kettle(object):
    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle('Kenwood', 100)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 200
print(kenwood.price)

hamilton = Kettle('Hamilton', 333)

print(f"Models: {kenwood.make} = {kenwood.price}, {hamilton.make} = {hamilton.price}")

print(type(kenwood))

print("-" * 50)
print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

print("-" * 50)
Kettle.switch_on(kenwood)
print(kenwood.on)

print("-" * 50)
print("Add new attribute not define in the class")
kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power) # Get an error AttributeError: 'Kettle' object has no attribute 'power'

print("-" * 50)
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print("+" * 25)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)

























