import math
from typing import Union
from calculator import base_models


CONSTANTS = base_models.CalculatorConstants

class Expression(base_models.Trigo):
    pass


def create_expression(start_value: Union[int, float, Expression]=0):
        return Expression(start_value=start_value)