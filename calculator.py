import math
from typing import Union, Literal, Self
from enum import Enum, auto
import base_models
from base_models import CalculatorConstants


class Expression(base_models.Trigo):
    pass


def create_expression(start_value: Union[int, float, Expression]=0):
        return Expression(start_value=start_value)