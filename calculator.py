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

class TrigoFunctions(Enum):
    SIN = "math.sin"
    COS = "math.cos"
    TAN = "math.tan"
    ASIN = "math.asin"
    ACOS = "math.acos"
    ATAN = "math.atan"


class HypTrigoFunctions(Enum):
    SINH = "math.sinh"
    COSH = "math.cosh"
    TANH = "math.tanh"
    ASINH = "math.asinh"
    ACOSH = "math.acosh"
    ATANH = "math.atanh"


class CalculatorExpression:

    def __init__(self, start_value: Union[int, float, "CalculatorExpression"]=0, mode=CalculatorConstants.DEGREE_MODE) -> None:
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

    def __operations_checker(self, operator):
        assert type(operator) in (str, CalculatorConstants)
        if type(operator) == str:
            return operator
        return operator.value

    def __value_checker(self, value):
        if type(value) in (int, float):
            return 0
        if type(value) is CalculatorExpression:
            return 1
        else: raise TypeError("Incorrect type of value. Value must be an expression object, int or float")

    def __trigo_builder(self, trigo, value):
        if trigo not in HypTrigoFunctions:
            if self.mode is CalculatorConstants.RADIAN_MODE:
                return f"{trigo.value}({value})"
            if trigo not in (TrigoFunctions.SIN, TrigoFunctions.COS, TrigoFunctions.TAN):
                return f"(math.degrees({trigo.value}({value})))"
            return f"{trigo.value}(math.radians({value}))"
        return f"{trigo.value}({value})"


    def __append_expression(self, operator: Literal["+", "-", "*", "/"], value: Union[int, str, "CalculatorExpression"], trigo: Union[TrigoFunctions, HypTrigoFunctions]=None):
        value_type = self.__value_checker(value)

        if trigo:
            if value_type == 0:
                self.__expression += f"{operator}{self.__trigo_builder(trigo,value)}"
            else: self.__expression += f"{operator}({self.__trigo_builder(trigo,value)})"
        
        elif value_type == 0:
            self.__expression += f"{operator}{value}"
        else: 
            self.__expression += f"{operator}({self.__trigo_builder(trigo,value)})"


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

    def sin(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.__append_expression(operator=confirmed_operator, value=value, trigo=TrigoFunctions.SIN)
        return self

    def cos(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.__append_expression(operator=confirmed_operator, value=value, trigo=TrigoFunctions.COS)
        return self

    def tan(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.__append_expression(operator=confirmed_operator, value=value, trigo=TrigoFunctions.TAN)
        return self

    def asin(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.__append_expression(operator=confirmed_operator, value=value, trigo=TrigoFunctions.ASIN)
        return self
    
    def acos(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.__append_expression(operator=confirmed_operator, value=value, trigo=TrigoFunctions.ACOS)
        return self

    def atan(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.__append_expression(operator=confirmed_operator, value=value, trigo=TrigoFunctions.ATAN)
        return self
    
    def sinh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.__append_expression(operator=confirmed_operator, value=value, trigo=HypTrigoFunctions.SINH)
        return self

    def cosh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.__append_expression(operator=confirmed_operator, value=value, trigo=HypTrigoFunctions.COSH)
        return self

    def tanh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.__append_expression(operator=confirmed_operator, value=value, trigo=HypTrigoFunctions.TANH)
        return self

    def asinh(self, operator:Union[Literal["+", "-", "*", "/"], CalculatorConstants], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.__append_expression(operator=confirmed_operator, value=value, trigo=HypTrigoFunctions.ASINH)
        return self
    
    def acosh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.__append_expression(operator=confirmed_operator, value=value, trigo=HypTrigoFunctions.ACOSH)
        return self

    def atanh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.__append_expression(operator=confirmed_operator, value=value, trigo=HypTrigoFunctions.ATANH)
        return self


    def clear_expression(self) -> Self:
        self.__expression = ""
        return self


    def evaluate(self) -> Union[int, float]:
        code = compile(self.__expression, "<string>", "eval")
        self.__answer = eval(code, {"__builtins__": {}, "math": math}, {})
        return self.answer


def create_expression(start_value: Union[int, float, "CalculatorExpression"]=0):
        return CalculatorExpression(start_value=start_value)