import math
from typing import Union, Literal, Self, Type
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


    def __operations_checker(self, operator):
        assert type(operator) in (str, CalculatorConstants)
        if type(operator) == str:
            return operator
        return operator.value
    
    def __append_expression(self, operator: CalculatorConstants, value: Union[int, str, "BaseExpression"], value_type: Literal[0,1]):
        parsed_operator = self.__operations_checker(operator)
        if value_type == 0:
            self.__expression += f"{parsed_operator}{value}"    
        else: self.__expression += f"{parsed_operator}({value})"

    
    def add(self, value: Union[int, float, "BaseExpression"]) -> Self:
        value_type = self.__value_checker(value)
        self.__append_expression(parsed_operator="+", value=value, value_type=value_type)
        return self
    
    def subtract(self, value: Union[int, float, "BaseExpression"]) -> Self:
        value_type = self.__value_checker(value)
        self.__append_expression(parsed_operator="-", value=value, value_type=value_type)
        return self

    def multiply(self, value: Union[int, float, "BaseExpression"]) -> Self:
        value_type = self.__value_checker(value)
        self.__append_expression(parsed_operator="*", value=value, value_type=value_type)
        return self

    def divide(self, value: Union[int, float, "BaseExpression"]) -> Self:
        value_type = self.__value_checker(value)
        self.__append_expression(parsed_operator="/", value=value, value_type=value_type)
        return self

    def pow(self, operator, value, index):
        value_type = self.__value_checker(value)
        self.__append_expression(parsed_operator=operator, value=f"math.pow({value}, {index})", value_type=value_type)

        
    def clear_expression(self) -> Self:
        self.__expression = ""
        return self


    def evaluate(self) -> Union[int, float]:
        code = compile(self.__expression, "<string>", "eval")
        self.__answer = eval(code, {"__builtins__": {}, "math": math}, {})
        return self.answer


class Trigo(BaseExpression):

    def __trigo_builder(self, trigo: Union[TrigoFunctions, HypTrigoFunctions], value: Union[int, float, Type[BaseExpression]]):
        if trigo not in HypTrigoFunctions:
            if self.mode is CalculatorConstants.RADIAN_MODE:
                return f"{trigo.value}({value})"
            if trigo not in (TrigoFunctions.SIN, TrigoFunctions.COS, TrigoFunctions.TAN):
                return f"(math.degrees({trigo.value}({value})))"
            return f"{trigo.value}(math.radians({value}))"
        return f"{trigo.value}({value})"

    def sin(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, Type[BaseExpression]]):
        parsed_operator = self.__operations_checker(operator)
        trigo_value = self.__trigo_builder(trigo=TrigoFunctions.SIN, value=value)
        self.__append_expression(operator=parsed_operator, value=trigo_value)
        return self

    def cos(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, Type[BaseExpression]]):
        parsed_operator = self.__operations_checker(operator)
        trigo_value = self.__trigo_builder(trigo=TrigoFunctions.COS, value=value)
        self.__append_expression(operator=parsed_operator, value=trigo_value)
        return self

    def tan(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, Type[BaseExpression]]):
        parsed_operator = self.__operations_checker(operator)
        trigo_value = self.__trigo_builder(trigo=TrigoFunctions.TAN, value=value)
        self.__append_expression(operator=parsed_operator, value=trigo_value)
        return self

    def asin(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, Type[BaseExpression]]):
        parsed_operator = self.__operations_checker(operator)
        trigo_value = self.__trigo_builder(trigo=TrigoFunctions.ASIN, value=value)
        self.__append_expression(operator=parsed_operator, value=trigo_value)
        return self
    
    def acos(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, Type[BaseExpression]]):
        parsed_operator = self.__operations_checker(operator)
        trigo_value = self.__trigo_builder(trigo=TrigoFunctions.ACOS, value=value)
        self.__append_expression(operator=parsed_operator, value=trigo_value)
        return self

    def atan(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, Type[BaseExpression]]):
        parsed_operator = self.__operations_checker(operator)
        trigo_value = self.__trigo_builder(trigo=TrigoFunctions.ATAN, value=value)
        self.__append_expression(operator=parsed_operator, value=trigo_value)
        return self
    
    def sinh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, Type[BaseExpression]]):
        parsed_operator = self.__operations_checker(operator)
        trigo_value = self.__trigo_builder(trigo=HypTrigoFunctions.SINH, value=value)
        self.__append_expression(operator=parsed_operator, value=trigo_value)
        return self

    def cosh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, Type[BaseExpression]]):
        parsed_operator = self.__operations_checker(operator)
        trigo_value = self.__trigo_builder(trigo=HypTrigoFunctions.COSH, value=value)
        self.__append_expression(operator=parsed_operator, value=trigo_value)
        return self

    def tanh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, Type[BaseExpression]]):
        parsed_operator = self.__operations_checker(operator)
        trigo_value = self.__trigo_builder(trigo=HypTrigoFunctions.TANH, value=value)
        self.__append_expression(operator=parsed_operator, value=trigo_value)
        return self

    def asinh(self, operator:Union[Literal["+", "-", "*", "/"], CalculatorConstants], value: Union[int, float, Type[BaseExpression]]):
        parsed_operator = self.__operations_checker(operator)
        trigo_value = self.__trigo_builder(trigo=HypTrigoFunctions.ASINH, value=value)
        self.__append_expression(operator=parsed_operator, value=trigo_value)
        return self
    
    def acosh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, Type[BaseExpression]]):
        parsed_operator = self.__operations_checker(operator)
        trigo_value = self.__trigo_builder(trigo=HypTrigoFunctions.ACOSH, value=value)
        self.__append_expression(operator=parsed_operator, value=trigo_value)
        return self

    def atanh(self, operator:Literal["+", "-", "*", "/"], value: Union[int, float, Type[BaseExpression]]):
        parsed_operator = self.__operations_checker(operator)
        trigo_value = self.__trigo_builder(trigo=HypTrigoFunctions.TANH, value=value)
        self.__append_expression(operator=parsed_operator, value=trigo_value)
        return self