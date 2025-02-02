# •	8. Design a system where a base class `Animal` has a method `speak()`, and subclasses `Dog` and `Cat` override it.
class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def speak(self):
        return "Dog barks"
class Cat(Animal):
    def speak(self):
        return "Cat meows"
obj = Dog()
print(obj.speak())
obj = Cat()
print(obj.speak())
