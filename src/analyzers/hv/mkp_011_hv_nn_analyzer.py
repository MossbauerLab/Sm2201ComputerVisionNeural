from src.devices.hv.hv_device import *
from src.analyzers.hv.hv_supply_nn_analyzer import *


class Mkp011HvNnAnalyzer(HvSupplyNnAnalyzer):
    def __init__(self):
        pass

    def analyze_state(self, *args, **kwargs):
        """
            Mkp-011 Neural Network analyzer. We suppose that device was already recognized as МКП-011
        :param args:
        :param kwargs:
            Keys:
                IMAGE - is a prepared image (trimmed zone with original colors and linearly transformed if angle of
                a view is not 90 degrees
        :return: An instance of HvDevice with state of Mkp-011 Hv Supply
        """
        hv_device = HvDevice()
        # 1. obtain image
        # 2. find LEDs group positions or use predefined values ???
        # 3. for each lead - take zone, make convolution and normalize by selecting only red channel
        # do it inside separate class for code re-use
        # 4. Based on three LEDs state define the state of object
        return hv_device

    __IMAGE_KEY = "IMAGE"

