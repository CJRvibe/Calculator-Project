import math
from typing import Union, Literal, Type
from enum import Enum, auto

class CalculatorConstants(Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"

class ExpressionConstants(Enum):
    SIN = "math.sin"
    COS = "math.cos"
    TAN = "math.tan"
    ASIN = "math.asin"
    ACOS = "math.acos"
    ATAN = "math.atan"
    SINH = "math.sinh"
    COSH = "math.cosh"
    TANH = "math.tanh"
    ASINH = "math.asinh"
    ACOSH = "math.acosh"
    ATANH = "math.atanh"


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
    
    
    def __operations_checker(self, operator):
        assert type(operator) in (str, CalculatorConstants)
        if type(operator) == str:
            return operator
        return operator.value

    def number_checker(self, value):
        assert type(value) in (int, float, CalculatorExpression)


    def append_expression(self, operator: Literal["+", "-", "*", "/"], value: Union[int, str, "CalculatorExpression"], trigo: ExpressionConstants=None):
        self.number_checker(value)
        if trigo:
            if type(value) is not CalculatorExpression:
                self.__expression += f"{operator}{trigo.value}({value})"
            else:
                self.__expression += f"{operator}({trigo.value}({value.expression}))"
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
        self.append_expression(operator=confirmed_operator, value=value, trigo=ExpressionConstants.SIN)
        return self

    def cos(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=ExpressionConstants.COS)
        return self

    def tan(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=ExpressionConstants.TAN)
        return self

    def asin(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=ExpressionConstants.ASIN)
        return self
    
    def acos(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=ExpressionConstants.ACOS)
        return self

    def atan(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=ExpressionConstants.ATAN)
        return self
    
    def sinh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=ExpressionConstants.SINH)
        return self

    def cosh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=ExpressionConstants.COSH)
        return self

    def tanh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=ExpressionConstants.TANH)
        return self

    def asinh(self, operator:Union[Literal["+", "-", "*", "/"], CalculatorConstants], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=ExpressionConstants.ASINH)
        return self
    
    def acosh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=ExpressionConstants.ACOSH)
        return self

    def atanh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, "CalculatorExpression"]):
        confirmed_operator = self.__operations_checker(operator)
        self.append_expression(operator=confirmed_operator, value=value, trigo=ExpressionConstants.ATANH)
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

    def create_expression(self, start_value: Union[int, float, "CalculatorExpression"]=0):
         return CalculatorExpression(start_value=start_value)
