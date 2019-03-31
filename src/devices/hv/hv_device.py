from abc import *


class HvDevice(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_state(self):
        pass

    def get_voltage(self):
        pass

    def get_polarity(self):
        pass

