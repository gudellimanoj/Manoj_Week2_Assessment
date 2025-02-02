class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model=model
    def display(self):
        return f"{self.brand} {self.model}"
class Car(Vehicle):
    def __init__(self,brand,model,fuel_type):
        super().__init__(brand,model)
        self.fuel_type=fuel_type
    def car_info(self):
        return f"{super().display()} is a {self.fuel_type} car"
class Bike(Vehicle):
    def __init__(self,brand,model,cc):
        super().__init__(brand,model)
        self.cc=cc
    def bike_info(self):
        return f"{super().display()} is a {self.cc} cc bike"
    
class EletricCar(Car):
    def __init__(self,brand,model,fuel_type,range):
        super().__init__(brand,model,fuel_type)
        self.range=range
    def eletric_car_info(self):
        return f"{super().car_info()} has a range of {self.range} km"
vehicle=Vehicle("Benz","top-end")
print(vehicle.display())
car=Car("Benz","topend","desiel")
print(car.car_info())
bike=Bike("Benz","top",500)
print(bike.bike_info())
eletric_car=EletricCar("Benz","top-end","desiel",100)
print(eletric_car.eletric_car_info())

# Reading input from the user
# def get_input():
#     brand = input("Enter brand: ")
#     model = input("Enter model: ")
#     fuel_type = input("Enter fuel type: ")
#     cc=int(input('Enter the bike cc'))
#     range=int(input('Enter the eletric car range'))
#     return brand,model,fuel_type,cc,range
# def main():
#     brand,model,fuel_type,cc,range=get_input()
#     car=Car(brand,model,fuel_type)
#     print(car.car_info())
#     bike=Bike(brand,model,cc)
#     print(bike.bike_info())
#     eletric_car=EletricCar(brand,model,fuel_type,range)
#     print(eletric_car.eletric_car_info())
# main()
