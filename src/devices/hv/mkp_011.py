from src.devices.hv.hv_device import HvDevice

"""
   Particular (existing model) of High Voltage Supply - МКП 011
"""


class Mkp011(HvDevice):

    def __init__(self):
        pass

    def get_powering_state(self):
        pass

    def is_overloading_present(self):
        return True

    def get_overload_state(self):
        pass

    def is_voltage_present(self):
        return False

    def get_voltage(self):
        pass

    def is_polarity_present(self):
        return True

    def get_polarity(self):
        pass

    def set_state(self, *args, **kwargs):
        pass
