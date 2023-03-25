import math
from enum import Enum
from typing import Union, Literal, Type
from .base_models import BaseExpression, CalculatorConstants


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


class Trigo(BaseExpression):

    def trigo_builder(self, trigo: Union[TrigoFunctions, HypTrigoFunctions], value: Union[int, float, Type[BaseExpression]]):
        if trigo not in HypTrigoFunctions:
            if self.mode is CalculatorConstants.RADIAN_MODE:
                return f"{trigo.value}({value})"
            if trigo not in (TrigoFunctions.SIN, TrigoFunctions.COS, TrigoFunctions.TAN):
                return f"(math.degrees({trigo.value}({value})))"
            return f"{trigo.value}(math.radians({value}))"
        return f"{trigo.value}({value})"

    def sin(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, Type[BaseExpression]]):
        value_type = self.value_checker(value)
        parsed_operator = self.operations_checker(operator)
        trigo_value = self.trigo_builder(trigo=TrigoFunctions.SIN, value=value)
        self.append_expression(operator=parsed_operator, value=trigo_value, value_type=value_type)
        return self

    def cos(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, Type[BaseExpression]]):
        value_type = self.value_checker(value)
        parsed_operator = self.operations_checker(operator)
        trigo_value = self.trigo_builder(trigo=TrigoFunctions.COS, value=value)
        self.append_expression(operator=parsed_operator, value=trigo_value, value_type=value_type)
        return self

    def tan(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, Type[BaseExpression]]):
        value_type = self.value_checker(value)
        parsed_operator = self.operations_checker(operator)
        trigo_value = self.trigo_builder(trigo=TrigoFunctions.TAN, value=value)
        self.append_expression(operator=parsed_operator, value=trigo_value, value_type=value_type)
        return self

    def asin(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, Type[BaseExpression]]):
        value_type = self.value_checker(value)
        parsed_operator = self.operations_checker(operator)
        trigo_value = self.trigo_builder(trigo=TrigoFunctions.ASIN, value=value)
        self.append_expression(operator=parsed_operator, value=trigo_value, value_type=value_type)
        return self
    
    def acos(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, Type[BaseExpression]]):
        value_type = self.value_checker(value)
        parsed_operator = self.operations_checker(operator)
        trigo_value = self.trigo_builder(trigo=TrigoFunctions.ACOS, value=value)
        self.append_expression(operator=parsed_operator, value=trigo_value, value_type=value_type)
        return self

    def atan(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, Type[BaseExpression]]):
        value_type = self.value_checker(value)
        parsed_operator = self.operations_checker(operator)
        trigo_value = self.trigo_builder(trigo=TrigoFunctions.ATAN, value=value)
        self.append_expression(operator=parsed_operator, value=trigo_value, value_type=value_type)
        return self
    
    def sinh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, Type[BaseExpression]]):
        value_type = self.value_checker(value)
        parsed_operator = self.operations_checker(operator)
        trigo_value = self.trigo_builder(trigo=HypTrigoFunctions.SINH, value=value)
        self.append_expression(operator=parsed_operator, value=trigo_value, value_type=value_type)
        return self

    def cosh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, Type[BaseExpression]]):
        value_type = self.value_checker(value)
        parsed_operator = self.operations_checker(operator)
        trigo_value = self.trigo_builder(trigo=HypTrigoFunctions.COSH, value=value)
        self.append_expression(operator=parsed_operator, value=trigo_value, value_type=value_type)
        return self

    def tanh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, Type[BaseExpression]]):
        value_type = self.value_checker(value)
        parsed_operator = self.operations_checker(operator)
        trigo_value = self.trigo_builder(trigo=HypTrigoFunctions.TANH, value=value)
        self.append_expression(operator=parsed_operator, value=trigo_value, value_type=value_type)
        return self

    def asinh(self, operator:Union[Literal["+", "-", "*", "/"], CalculatorConstants], value: Union[int, float, Type[BaseExpression]]):
        value_type = self.value_checker(value)
        parsed_operator = self.operations_checker(operator)
        trigo_value = self.trigo_builder(trigo=HypTrigoFunctions.ASINH, value=value)
        self.append_expression(operator=parsed_operator, value=trigo_value, value_type=value_type)
        return self
    
    def acosh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, Type[BaseExpression]]):
        value_type = self.value_checker(value)
        parsed_operator = self.operations_checker(operator)
        trigo_value = self.trigo_builder(trigo=HypTrigoFunctions.ACOSH, value=value)
        self.append_expression(operator=parsed_operator, value=trigo_value, value_type=value_type)
        return self

    def atanh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, Type[BaseExpression]]):
        value_type = self.value_checker(value)
        parsed_operator = self.operations_checker(operator)
        trigo_value = self.trigo_builder(trigo=HypTrigoFunctions.TANH, value=value)
        self.append_expression(operator=parsed_operator, value=trigo_value, value_type=value_type)
        return self