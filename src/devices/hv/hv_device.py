from abc import *

"""
    HvDevice is an abstract class for any detector HV supply.
    Plain data class representing state of HV Supply
"""


class HvDevice(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def set_state(self, *args, **kwargs):
        """
            Set state based on analyze state of particular HV with Neural Networks with Image processing
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError(u'abstract method')

    @abstractmethod
    def get_powering_state(self):
        raise NotImplementedError(u'abstract method')

    @abstractmethod
    def is_overloading_present(self):
        """
           Checking if HV has capabilities to control overloading (visual indication)
        :return:
        """
        return False

    @abstractmethod
    def get_overload_state(self):
        raise NotImplementedError(u'abstract method')

    @abstractmethod
    def is_voltage_present(self):
        """
           Checking if HV has capabilities to show voltage value (visual indication)
        :return:
        """
        return False

    @abstractmethod
    def get_voltage(self):
        raise NotImplementedError(u'abstract method')

    @abstractmethod
    def is_polarity_present(self):
        """
           Checking if HV has capabilities to control polarity of hv (visual indication)
        :return:
        """
        return False

    @abstractmethod
    def get_polarity(self):
        raise NotImplementedError(u'abstract method')

    __NEGATIVE_POLARITY = 1
    __POSITIVE_POLARITY = 2
