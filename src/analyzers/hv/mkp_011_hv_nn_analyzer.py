import os
import logging

import numpy
from keras.preprocessing import image
from keras.engine.saving import *
from keras.models import *
from keras.layers import *

from src.devices.hv.hv_device import *
from src.analyzers.hv.hv_supply_nn_analyzer import *


class Mkp011HvNnAnalyzer(HvSupplyNnAnalyzer):
    def __init__(self, model_path, nn_model=None):
        """
           Class constructor
        :param model_path: a path where to save / load trained model, names are predefined in __MODEL_FILE and
        __MODEL_WEIGHTS file
        :param nn_model: loaded keras nn model with loaded weights (trained neural network). Could be trained outside
        of DEVELOPING machine i.e. using GOOGLE Collaboratory of MS Jupyter Notebook
        """
        self._model_path = model_path
        self._nn_model = nn_model
        # TODO: umv: init logger
        if nn_model is None:
            # try load it from json ...
            try:
                model_file = open(os.path.join(self._model_path, self.__MODEL_FILE), u'r')
                model_json = model_file.read()
                model_file.close()
                self._nn_model = model_from_json(model_json)
                self._nn_model.load_weights(os.path.join(self._model_path, self.__MODEL_WEIGHTS_FILE))
            except Exception as e:
                # TODO: umv: log an error
                pass

    def train(self, train_data, export):
        """
            Train neural network on prepared train_data (format of trained data is not ready yet). After train model
            is placed in _nn_model and optionally could be export to json.
            We don't have learning_factor and OTHER PARAMETERS that ARE SUFFICIENT 4 training
        :param train_data:
            A bunch of image plus metadata for check ...
        :param export:
            A flag to export (save) trained model ...
        :return:
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

    __MODEL_FILE = u'mkp-011_keras_nn_model.json'
    __MODEL_WEIGHTS_FILE = u'mkp-011_keras_nn_model.h5'
    __IMAGE_KEY = u'IMAGE'

    _nn_model = None
    _model_file = u''
    _model_path = u''

