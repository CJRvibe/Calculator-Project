import math
from typing import Union, Literal

class Calculator:

    class __ExpressionStatement:
        def __init__(self) -> None:
            self.expression: str = ""


        def number_checker(self, number):
            assert type(number) in (int, float)


        def append_expression(self, number: Union[int, str], operator: Literal["+", "-", "*", "/"]):
            self.number_checker(number)
            self.expression += f"{operator}{number}"

        def evaluate(self):
            result = eval(self.expression, {"__builtins__": {}}, {})
            self.expression = "0"
            return result
    
    def __init__(self) -> None:
        self.answer: int = 0
        self.__expression = self.__ExpressionStatement()


    def add(self, number: Union[int, float]):
        self.__expression.append_expression(number, "+")
        return self
    
    def subtract(self, number: Union[int, float]):
        self.__expression.append_expression(number, "-")
        return self

    def multiply(self, number: Union[int, float]):
        self.__expression.append_expression(number, "*")
        return self

    def divide(self, number: Union[int, float]):
        self.__expression.append_expression(number, "/")
        return self


    def evaluate(self):
        self.answer = self.__expression.evaluate()
        return self.answer

    def raw_evaluate(self, expression: str):
        code = compile(expression, "<string>", "eval")
        if code.co_names:
            raise NameError("cannot use variable names in the expression")
        return eval(code, {"__builtins__": {}}, {})