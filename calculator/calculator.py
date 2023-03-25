import math
from typing import Union
from . import base_models
from . import power_model
from . import trigo_model


CONSTANTS = base_models.CalculatorConstants

class Expression(trigo_model.Trigo, power_model.Power):
    pass


def create_expression(start_value: Union[int, float, Expression]=0):
        return Expression(start_value=start_value)