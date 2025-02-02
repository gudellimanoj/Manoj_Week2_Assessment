# •	10. Build a `SmartPhone` class inheriting from `MobileDevice`, which in turn inherits from `Electronics`. Demonstrate method overriding and attribute reuse
class Electronics:
    def __init__(self, brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def display(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nPrice: {self.price}"
class MobileDevice(Electronics):
    def __init__(self, brand, model, price, os):
        super().__init__(brand, model, price)
        self.os = os
    def display(self):
        return f"{super().display()}\nOS: {self.os}"
class SmartPhone(MobileDevice):
    def __init__(self, brand, model, price, os, camera):
        super().__init__(brand, model, price, os)
        self.camera = camera
    def display(self):
        return f"{super().display()}\nCamera: {self.camera}"
obj = SmartPhone("Samsung", "Galaxy S21", 70000, "Android", "108 MP")
print(obj.display())
obj = MobileDevice("Apple", "iPhone 12", 80000, "iOS")
print(obj.display())
obj = Electronics("Sony", "Bravia", 50000)
print(obj.display())
