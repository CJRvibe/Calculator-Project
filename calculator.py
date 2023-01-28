import math
from typing import Union, Literal, Type
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

    def number_checker(self, value):
        assert type(value) in (int, float, CalculatorExpression)


    def append_expression(self, operator: Literal["+", "-", "*", "/"], value: Union[int, str, "CalculatorExpression"], trigo: Union[TrigoFunctions, HypTrigoFunctions]=None):
        self.number_checker(value)
        if trigo:
            if type(value) is not CalculatorExpression:
                if self.mode is not CalculatorConstants.RADIAN_MODE:
                    if trigo not in (TrigoFunctions.SIN, trigo.COS, TrigoFunctions.TAN):
                        self.__expression += f"{operator}(math.degrees({trigo.value}(math.radians({value}))))"
                    else:
                        self.__expression += f"{operator}{trigo.value}(math.radians({value}))"

            else:
                if self.mode is not CalculatorConstants.RADIAN_MODE:
                    if trigo not in (TrigoFunctions.SIN, trigo.COS, TrigoFunctions.TAN):
                        self.__expression += f"{operator}((math.degrees({trigo.value}(math.radians({value})))))"
                    else:
                        self.__expression += f"{operator}({trigo.value}(math.radians({value})))"
        else:
            if type(value) is not CalculatorExpression:
               self.__expression += f"{operator}{value}"
            else:
                self.__expression += f"{operator}({value.expression})"


    def add(self, value: Union[int, float, "CalculatorExpression"]):
        self.append_expression(operator="+", value=value)
        return self
    
    def subtract(self, value: Union[int, float, "CalculatorExpression"]):
        self.append_expression(operator="-", value=value)
        return self

    def multiply(self, value: Union[int, float, "CalculatorExpression"]):
        self.append_expression(operator="*", value=value)
        return self

    def divide(self, value: Union[int, float, "CalculatorExpression"]):
        self.append_expression(operator="/", value=value)
        return self


    def sin(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=TrigoFunctions.SIN)
        return self

    def cos(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=TrigoFunctions.COS)
        return self

    def tan(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=TrigoFunctions.TAN)
        return self

    def asin(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=TrigoFunctions.ASIN)
        return self
    
    def acos(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=TrigoFunctions.ACOS)
        return self

    def atan(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=TrigoFunctions.ATAN)
        return self
    
    def sinh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=HypTrigoFunctions.SINH)
        return self

    def cosh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=HypTrigoFunctions.COSH)
        return self

    def tanh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=HypTrigoFunctions.TANH)
        return self

    def asinh(self, operator:Union[Literal["+", "-", "*", "/"], CalculatorConstants], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=HypTrigoFunctions.ASINH)
        return self
    
    def acosh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=HypTrigoFunctions.ACOSH)
        return self

    def atanh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=HypTrigoFunctions.ATANH)
        return self


    def clear_expression(self):
        self.__expression = ""
        return self


    def evaluate(self) -> Union[int, float]:
        code = compile(self.__expression, "<string>", "eval")
        # if code.co_names:
        #     raise NameError("cannot use variable names in the expression")
        self.__answer = eval(code, {"__builtins__": {}, "math": math}, {})
        return self.answer



class Calculator:

    constants = CalculatorConstants

    def create_expression(self, start_value: Union[int, float, "CalculatorExpression"]=0, mode=CalculatorConstants.DEGREE_MODE):
         return CalculatorExpression(start_value=start_value, mode=mode)
