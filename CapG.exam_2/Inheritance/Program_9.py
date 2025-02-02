# •	9. Simulate multiple inheritance where `FlyingCar` inherits from both `Car` and `Airplane`. Handle potential conflicts in the `move()` method.
class Car:
    def move(self):
        return "Car moves on road"
class Airplane:
    def move(self):
        return "Airplane flies in the sky"
class FlyingCar(Car, Airplane):
    def move(self):
        return "FlyingCar moves in the sky"
flying_car=FlyingCar()
print(flying_car.move())  
car=Car()
print(car.move())
airplane=Airplane()
print(airplane.move())


