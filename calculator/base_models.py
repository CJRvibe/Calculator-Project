import math
from typing import Union, Literal, Self
from enum import Enum, auto


class CalculatorConstants(Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    DEGREE_MODE = 1
    RADIAN_MODE = 2


class BaseExpression:
    def __init__(self, start_value: Union[int, float, "BaseExpression"]=0, mode=CalculatorConstants.DEGREE_MODE) -> None:
        self.__expression: str = f"{start_value}"
        self.__answer: Union[int, float, None] = None
        self.__mode = mode

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode):
        if mode not in (CalculatorConstants.DEGREE_MODE, CalculatorConstants.RADIAN_MODE):
            raise TypeError("Use one of the values provided")
        self.__mode = mode


    @property
    def expression(self):
        return self.__expression

    @property
    def answer(self):
        return self.__answer

    
    def value_checker(self, value):
        if type(value) in (int, float):
            return 0
        if type(value) is BaseExpression:
            return 1
        else: raise TypeError("Incorrect type of value. Value must be an expression object, int or float")


    def operations_checker(self, operator):
        assert type(operator) in (str, CalculatorConstants)
        if type(operator) == str:
            return operator
        return operator.value
    
    def append_expression(self, operator: CalculatorConstants, value: Union[int, str, "BaseExpression"], value_type: Literal[0,1]):
        parsed_operator = self.operations_checker(operator)
        if value_type == 0:
            self.__expression += f"{parsed_operator}{value}"    
        else: self.__expression += f"{parsed_operator}({value})"

    
    def add(self, value: Union[int, float, "BaseExpression"]) -> Self:
        value_type = self.value_checker(value)
        self.append_expression(operator="+", value=value, value_type=value_type)
        return self
    
    def subtract(self, value: Union[int, float, "BaseExpression"]) -> Self:
        value_type = self.value_checker(value)
        self.append_expression(operator="-", value=value, value_type=value_type)
        return self

    def multiply(self, value: Union[int, float, "BaseExpression"]) -> Self:
        value_type = self.value_checker(value)
        self.append_expression(operator="*", value=value, value_type=value_type)
        return self

    def divide(self, value: Union[int, float, "BaseExpression"]) -> Self:
        value_type = self.value_checker(value)
        self.append_expression(operator="/", value=value, value_type=value_type)
        return self

    def pow(self, operator, value, index):
        value_type = self.value_checker(value)
        self.append_expression(operator=operator, value=f"math.pow({value}, {index})", value_type=value_type)

        
    def clear_expression(self) -> Self:
        self.__expression = ""
        return self


    def evaluate(self) -> Union[int, float]:
        code = compile(self.__expression, "<string>", "eval")
        self.__answer = eval(code, {"__builtins__": {}, "math": math}, {})
        return self.answer