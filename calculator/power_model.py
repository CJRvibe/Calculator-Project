import math
from .base_models import BaseExpression

class Power(BaseExpression):

    def sqrt(self, operator, value):
        value_type = self.value_checker(value)
        self.append_expression(operator, f"math.sqrt({value})", value_type)
        return self

    def cbrt(self, operator, value):
        value_type = self.value_checker(value)
        self.append_expression(operator, f"math.sqrt({value})", value_type)
        return self

    def lawn(self, operator, value):
        value_type = self.value_checker(value)
        self.append_expression(operator, f"math.log({value})", value_type)
        return self

    def log10(self, operator, value):
        value_type = self.value_checker(value)
        self.append_expression(operator, f"math.log10({value})", value_type)
        return self
        
    def exp_e(self, operator, value):
        value_type = self.value_checker(value)
        self.append_expression(operator, f"math.exp({value})", value_type)
        return self

    def exp_2(self, operator, value):
        value_type = self.value_checker(value)
        self.append_expression(operator, f"math.exp2({value})", value_type)
        return self
    