# •	18. Implement an abstract class `ICalculator` with methods `add()`, `subtract()`, `multiply()`, and `divide()`. Create a `BasicCalculator` class that implements these methods.

from abc import ABC, abstractmethod
class ICalculator(ABC):
    @abstractmethod
    def add(self, num1, num2):
        pass
    @abstractmethod
    def subtract(self, num1, num2):
        pass
    @abstractmethod
    def multiply(self, num1, num2):
        pass
    @abstractmethod
    def divide(self, num1, num2):
        pass
class BasicCalculator(ICalculator):
    def add(self, num1, num2):
        return f"Addition: {num1+num2}"
    def subtract(self, num1, num2):
        return f"Subtraction: {num1-num2}"
    def multiply(self, num1, num2):
        return f"Multiplication: {num1*num2}"
    def divide(self, num1, num2):
        return f"Division: {num1/num2}"
calculator = BasicCalculator()
print(calculator.add(5, 4))
print(calculator.subtract(5, 4))
print(calculator.multiply(5, 4))
print(calculator.divide(5, 4))
