import math
from typing import Union
class Calculator:
    
    def __init__(self) -> None:
        self.answer: int = 0
        self.expression: str = "0"

    
    def __number_checker(self, number):
        assert type(number) in (int, float)


    def add(self, number: Union[int, float]):
        self.__number_checker(number)
        self.expression += f" + {number}"
        return self

    
    def subtract(self, number: Union[int, float]):
        self.__number_checker(number)
        self.expression += f" - {number}"
        return self


    def multiply(self, number: Union[int, float]):
        self.__number_checker(number)
        self.expression += f" * {number}"
        return self
    

    def divide(self, number: Union[int, float]):
        self.__number_checker(number)
        self.expression += f" / {number}"
        return self


    def evaluate(self):
        self.answer = eval(self.expression, {"__builtins__": {}}, {})
        self.expression = "0"
        return self.answer



    def raw_evaluate(self, expression: str):
        code = compile(expression, "<string>", "eval")
        if code.co_names:
            raise NameError("cannot use variable names in the expression")
        return eval(code, {"__builtins__": {}}, {})