import math
from typing import Union, Literal, Type


class CalculatorExpression:

    def __init__(self) -> None:
        self.__expression: str = ""
        self.__answer: Union[int, float, None] = None

    @property
    def expression(self):
        return self.__expression

    @property
    def answer(self):
        return self.__answer
    
    
    def number_checker(self, value):
        assert type(value) in (int, float, CalculatorExpression)


    def append_expression(self, operator: Literal["+", "-", "*", "/"], value: Union[int, str, "CalculatorExpression"]):
        self.number_checker(value)
        if type(value) is not CalculatorExpression:
            self.__expression += f"{operator}{value}"
        else:
            self.__expression += f"{operator}({value.expression})"


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

    
    def sub_expression(self, operator: Literal["+", "-", "*", "/"], value: "CalculatorExpression"):
        if operator not in ("+", "-", "*", "/"):
            raise ValueError("Please specify a proper arithmetic operator")
        if type(value) is not CalculatorExpression:
            raise TypeError("Please enter a CalculatorExpression object in the value parameter")
        self.append_expression(operator=operator, value=value)
        return self


    def clear_expression(self):
        self.__expression = ""
        return self


    def evaluate(self) -> Union[int, float]:
        code = compile(self.__expression, "<string>", "eval")
        if code.co_names:
            raise NameError("cannot use variable names in the expression")
        self.__answer =  eval(code, {"__builtins__": {}}, {})
        return self.answer

class Calculator:

    def create__expression(self):
         return CalculatorExpression()
