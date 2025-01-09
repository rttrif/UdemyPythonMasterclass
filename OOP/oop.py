class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

kenwood = Kettle('Kenwood', 100)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 200
print(kenwood.price)

hamilton = Kettle('Hamilton', 333)

print(f"Models: {kenwood.make} = {kenwood.price}, {hamilton.make} = {hamilton.price}")