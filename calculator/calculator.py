import math
from typing import Union
import power_model
import base_models



class Constants(base_models.CalculatorConstants):
    pass

class Expression(base_models.Trigo, power_model.Power):
    pass


def create_expression(start_value: Union[int, float, Expression]=0):
        return Expression(start_value=start_value)