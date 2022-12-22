from math import *
import numpy as np

values = ["0", "0", "0", "0", "0", "0"]

oi = float
ov = float
ow = float
si = float
sv = float
sw = float

class Transformer():
    def __init__(self, oi, ov, ow, si, sv, sw):
        self.oi = oi
        self.ov = ov
        self.ow = ow
        self.si = si
        self.sv = sv
        self.sw = sw
             
    def current_w(self):
        return round(ow / ov, 2)

    def current_m(self):
        return round(sqrt(oi**2 - data.current_w()**2), 2)

    def resistance_o(self):
        return round(ov / data.current_w(), 2)

    def impedence_o(self):
        return round(ov / data.current_m(), 2)

    def resistance_o1(self):
        return round(sw / si**2, 2)

    def impedence_o1(self):
        reactance = sv / si
        return round(sqrt(reactance**2 - data.resistance_o1()**2), 2)

    def power_factor(self):
        return ow / (ov*oi)


data = Transformer(values[0], values[1], values[2], values[3], values[4], values[5])

def print_calculation():
    
    current_w_result = "Iw: %s A" % data.current_w()
    print(current_w_result)
    current_m_result = "Iμ: %s A" % data.current_m()
    print(current_m_result)
    resistance_o_result = "Ro: %s Ω" % data.resistance_o()
    print(resistance_o_result)
    impedence_o_result = "Xo: %s Ω" % data.impedence_o()
    print(impedence_o_result)
    resistance_o1_result = "Ro1: %s Ω" % data.resistance_o1()
    print(resistance_o1_result)
    impedence_o1_result = "Xo1: %s Ω" % data.impedence_o1()
    print(impedence_o1_result)
    power_factor_result = "Cosφ: %s" % data.power_factor()
    print(power_factor_result)

    return current_w_result, current_m_result, resistance_o_result, impedence_o_result, resistance_o1_result, impedence_o1_result, power_factor_result