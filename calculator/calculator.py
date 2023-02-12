import math
from typing import Union
import calculator.base_models as base_models


class Constants(base_models.CalculatorConstants):
    pass

class Expression(base_models.Trigo):
    pass


def create_expression(start_value: Union[int, float, Expression]=0):
        return Expression(start_value=start_value)