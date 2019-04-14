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


class HvSupplyNnAnalyzer(ABC):
    def __init(self):
        pass

    @abstractmethod
    def train(self):
        raise NotImplementedError(u'train is an abstract method')

    @abstractmethod
    def analyze_state(self, *args, **kwargs):
        """
            Analyze state based on CV with keras
        :param args:
        :param kwargs:
        :return: Should return instance of HvDevice
        """
        raise NotImplementedError(u'analyze_state is an abstract method')

