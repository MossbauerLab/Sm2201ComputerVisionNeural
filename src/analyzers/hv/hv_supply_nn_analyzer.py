from abc import *

"""
   Common interface for Detector High Voltage Supply Analyzer:
   What could we Analyze:
       1) State (is powering detector or not) - HV indication presence
       2) Overload (some HV has overload indication)
       3) Polarity of HV Supply (neg or pos)
       4) Voltage
    Any particular HV has OWN interface sets
"""


class HvSupplyNnAnalyzer(object):
    def __init(self):
        pass

    def analyze_state(self, *args, **kwargs):
        pass

    __NEGATIVE_POLARITY = 1
    __POSITIVE_POLARITY = 2
