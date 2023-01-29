import math
from typing import Union, Literal, Self


class CalculatorExpression:

    def __init__(self, start_value: Union[int, float, "CalculatorExpression"]=0) -> None:
        self.__expression: str = f"{start_value}"
        self.__answer: Union[int, float, None] = None

    @property
    def expression(self):
        return self.__expression

    @property
    def answer(self):
        return self.__answer
    
    
    def __number_checker(self, value):
        assert type(value) in (int, float, CalculatorExpression)


    def __append_expression(self, operator: Literal["+", "-", "*", "/"], value: Union[int, str, "CalculatorExpression"]):
        self.__number_checker(value)
        if type(value) is not CalculatorExpression:
            self.__expression += f"{operator}{value}"
        else:
            self.__expression += f"{operator}({value.expression})"


    def add(self, value: Union[int, float, "CalculatorExpression"]) -> Self:
        self.__append_expression(operator="+", value=value)
        return self
    
    def subtract(self, value: Union[int, float, "CalculatorExpression"]) -> Self:
        self.__append_expression(operator="-", value=value)
        return self

    def multiply(self, value: Union[int, float, "CalculatorExpression"]) -> Self:
        self.__append_expression(operator="*", value=value)
        return self

    def divide(self, value: Union[int, float, "CalculatorExpression"]) -> Self:
        self.__append_expression(operator="/", value=value)
        return self

    def pow(self, operator, value, index):
        self.__expression += f"{operator}math.pow({value}, {index})"

    def clear_expression(self) -> Self:
        self.__expression = ""
        return self


    def evaluate(self) -> Union[int, float]:
        code = compile(self.__expression, "<string>", "eval")
        self.__answer = eval(code, {"__builtins__": {}, "math": math}, {})
        return self.answer


def create_expression(start_value: Union[int, float, "CalculatorExpression"]=0):
        return CalculatorExpression(start_value=start_value)
