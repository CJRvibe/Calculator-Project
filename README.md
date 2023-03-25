# Calculator-Project
A small calculator project created to test my programming skills. The calculator implemenmts lazy evaluation. This means that you build up the expression first, then evaluate it.

## Simple Usage
```py
import calculator
from calculator import CONSTANTS

exp = calculator.Expression(start_value=0, mode=CONSTANTS.RADIAN_MODE)
exp = calculator.create_expresion(start_value=0, mode=CONSTANTS.RADIAN_MODE) # This works as well

exp.add(5).multiply(6).subtract(10) # hook multiple methods together

exp.expression # To take a look at the current expression build up

answer = exp.evaluate()
answer = exp.answer # You can also get the answer here

exp.clear_expression() # Always clear the expression else the old expression is still there
```
