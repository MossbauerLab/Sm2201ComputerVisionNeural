from keras.models import Sequential
from keras.layers import Dense, Activation

"""
    LED state analyzer neural network
"""


class LedAnalyzer(object):
    def __init__(self, model_path=u'./nn_models', nn_model=None):
        """
            Simple LED analyzer
        :param model_path:
        :param nn_model:
        """
        # TODO: umv: implement model loading
        pass

    def train(self, train_data, export):
        """
           Train neural network to analyze LED state.
           Guide to build sequential model is here: https://keras.io/getting-started/sequential-model-guide/
           Model is:
              INPUT - image 64x64 with 3 bytes (RGB)
              LAYER1 - output - binary value 'is led on image or not'
              LAYER2 - (should be connected with LAYER1 and input) - led state analyser
              OUTPUT - Tuple (is_led: True/False, led_state: None/True/False)
        :param train_data:
        :param export:
        :return:
        """
        model = Sequential([
            # Dense(input_dim=(3, self.__INPUT_LAYER_DEFAULT_DENSITY, self.__INPUT_LAYER_DEFAULT_DENSITY), output_dim=2)
        ])
        pass

    def analyze(self, *args, **kwargs):
        pass

    __MODEL_FILE = u'led_keras_nn_model.json'
    __MODEL_WEIGHTS_FILE = u'led_keras_nn_model.h5'
    __IMAGE_KEY = u'IMAGE'
    __INPUT_LAYER_DEFAULT_DENSITY = 64

    _nn_model = None
    _model_path = u''
