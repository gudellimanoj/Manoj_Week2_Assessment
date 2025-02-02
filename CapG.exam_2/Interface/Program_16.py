# •	16. Create an interface `IShape` with an abstract method `calculate_area()`. Implement it in `Rectangle` and `Circle` classes.
from abc import ABC, abstractmethod
class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class Rectangle(IShape):
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth    
    def calculate_area(self):
        return f"Area of rectangle: {self.length*self.breadth}"
class Circle(IShape):
    def __init__(self, radius):
        self.radius=radius
    def calculate_area(self):
        return f"Area of circle: {3.14*self.radius*self.radius}"
rectangle = Rectangle(5, 4)
print(rectangle.calculate_area())
circle = Circle(5)
print(circle.calculate_area())

