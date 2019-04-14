# from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Dense
import numpy

from src.devices.hv.hv_device import *
from src.analyzers.hv.hv_supply_nn_analyzer import *


class Mkp011HvNnAnalyzer(HvSupplyNnAnalyzer):
    def __init__(self, model_path, model=None):
        """
           Class constructor
        :param model_path: a path where to save trained model
        :param model: model json
        """
        self._model_path = model_path
        self._model = model
        if model is not None:
            # try load it from json ...
            pass

    def train(self):
        """
           train, produce model file (json)
        :return: None
        """
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

    _model = u''
    _model_path = u''

