import math
from typing import Union, Literal


class CalculatorExpression:
    
    def __init__(self) -> None:
        self.__expression: str = ""
        self.__answer: Union[int, float, None] = None

    @property
    def expression(self):
        return self.__expression

    @property
    def answer(self):
        self.__answer
    
    
    def number_checker(self, value):
        assert type(value) in (int, float, CalculatorExpression)


    def append_expression(self, operator: Literal["+", "-", "*", "/"], value: Union[int, str]):
        self.number_checker(value)
        self.__expression += f"{operator}{value}"


    def add(self, value: Union[int, float]):
        self.append_expression(operator="+", value=value)
        return self
    
    def subtract(self, value: Union[int, float]):
        self.append_expression(operator="-", value=value)
        return self

    def multiply(self, value: Union[int, float]):
        self.append_expression(operator="*", value=value)
        return self

    def divide(self, value: Union[int, float]):
        self.append_expression(operator="/", value=value)
        return self


    def clear_expression(self):
        self.__expression = ""
        return self


    def evaluate(self):
        code = compile(self.__expression, "<string>", "eval")
        if code.co_names:
            raise NameError("cannot use variable names in the expression")
        answer = eval(code, {"__builtins__": {}}, {})
        return answer

class Calculator:

    def create__expression(self):
         return CalculatorExpression()
