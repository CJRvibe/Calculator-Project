import math

class Calculator:
    
    def __init__(self) -> None:
        pass


    def raw_evaluate(self, expression: str):
        code = compile(expression, "<string>", "eval")
        if code.co_names:
            raise NameError("cannot use variable names in the expression")
        return eval(code, {"__builtins__": {}}, {})