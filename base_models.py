import math
from typing import Union, Literal, Self
from enum import Enum, auto


class CalculatorConstants(Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    DEGREE_MODE = auto()
    RADIAN_MODE = auto()


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

    
    def __value_checker(self, value):
        if type(value) in (int, float):
            return 0
        if type(value) is BaseExpression:
            return 1
        else: raise TypeError("Incorrect type of value. Value must be an expression object, int or float")

    
    def __append_expression(self, operator: CalculatorConstants, value: Union[int, str, "BaseExpression"], value_type: Literal[0,1]):
        if value_type == 0:
            self.__expression += f"{operator}{value}"    
        else: self.__expression += f"{operator}({value})"

        
    def clear_expression(self) -> Self:
        self.__expression = ""
        return self


    def evaluate(self) -> Union[int, float]:
        code = compile(self.__expression, "<string>", "eval")
        self.__answer = eval(code, {"__builtins__": {}, "math": math}, {})
        return self.answer


