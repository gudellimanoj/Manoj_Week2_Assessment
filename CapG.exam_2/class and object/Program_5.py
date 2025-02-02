# Create a `Product` class with attributes `name`, `price`, and `stock`. Write a method `check_availability(quantity)` that returns whether the requested quantity is available.
class Product:
     def __init__(self, name, price, stock):
         self.name=name
         self.price=price
         self.stock=stock
     def check_availability(self, quantity):
         if quantity<=self.stock:
             return "Available"
         else:
             return "Not Available"
obj =Product("Laptop", 50000, 10)
print(obj.check_availability(5))
print(obj.check_availability(20))


class Product:
    def __init__(self, name, price, stock):
        self.name=name
        self.price=price
        self.stock=stock
    def check_avialability(self,quantity):
        if quantity<=self.stock:
            return "Available"
        else:
            return "Not Avialable"
obj=Product("LP",60000, 10)
print(obj.check_avialability(5))
print(obj.check_avialability(20))
