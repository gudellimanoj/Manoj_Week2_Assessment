# •	13. Develop a `Shape` class with a method `area()`. Implement `Square` and `Triangle` classes that provide specific implementations for `area()`.
class Shape:
    def area(self):
        return "Area of shape"
class Square(Shape):
    def area(self, side):
        return f"Area of square: {side*side}"
class Triangle(Shape):
    def area(self, base, height):
        return f"Area of triangle: {0.5*base*height}"
obj = Square()
print(obj.area(5))
obj = Triangle()
print(obj.area(3, 4))


