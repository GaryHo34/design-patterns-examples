from enum import Enum
# python 3.8 and above
from typing import Protocol, Dict

class IOperatorStrategy(Protocol):
    def calculate(self, a: int, b: int) -> int:
        pass

class AddStrategy(IOperatorStrategy):
    def calculate(self, a: int, b: int) -> int:
        print(f"The result of {a} + {b} = {a + b}")
        return a + b

class SubtractStrategy(IOperatorStrategy):
    def calculate(self, a: int, b: int) -> int:
        print(f"The result of {a} - {b} = {a - b}")
        return a - b

class MultiplyStrategy(IOperatorStrategy):
    def calculate(self, a: int, b: int) -> int:
        print(f"The result of {a} * {b} = {a * b}")
        return a * b
    
class DivideStrategy(IOperatorStrategy):
    def calculate(self, a: int, b: int) -> int:
        print(f"The result of {a} / {b} = {a / b}")
        return a / b
    
# a class calculator is our context
# set a private strategy field
class Calculator:
    def __init__(self, strategy: IOperatorStrategy):
        self._strategy = strategy
    def setStrategy(self, strategy: IOperatorStrategy):
        self._strategy = strategy
    def calculate(self, a: int, b: int) -> int:
        return self._strategy.calculate(a, b)

# test as a client 
if __name__ == "__main__":
    calculator = Calculator(AddStrategy())
    calculator.calculate(1, 2)
    
    calculator.setStrategy(SubtractStrategy())
    calculator.calculate(1, 2)
    
    calculator.setStrategy(MultiplyStrategy())
    calculator.calculate(1, 2)

    calculator.setStrategy(DivideStrategy())
    calculator.calculate(1, 2)