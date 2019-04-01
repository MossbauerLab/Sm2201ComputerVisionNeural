"""
    HvDevice is a common class for any detector HV supply.  Plain data class representing state of HV Supply
"""


class HvDevice(object):
    def __init__(self):
        pass

    def set_state(self, **kwargs):
        """
            Set state based on analyze state of particular HV with Neural Networks with Image processing
        :param kwargs:
            Keys:
                  HV_TYPE = HV name (i.e. МКП 011)
                  POLARITY = None / __NEGATIVE_POLARITY / __POSITIVE_POLARITY
                  POWERING_STATE = True / False, True means that HW supply is working
                  OVERLOADING_STATE = True / False, True means that HV is overloaded and it should be reloaded
                  VOLTAGE = Double value /None
            REQUIRED KEY is only POWERING_STATE
        :return:
        """
        # save required value
        if self.__POWERING_STATE_KEY not in kwargs:
            raise RuntimeError(u'Required named parameter (\'{0}\') was not passed'.format(self.__POWERING_STATE_KEY))
        self._powering_state = kwargs[self.__POWERING_STATE_KEY]
        # save optional values
        if self.__HV_TYPE_KEY in kwargs:
            self._hv_type = kwargs[self.__HV_TYPE_KEY]
        if self.__VOLTAGE_KEY in kwargs:
            self._voltage_value = kwargs[self.__VOLTAGE_KEY]
        if self.__POLARITY_KEY in kwargs:
            self._polarity = kwargs[self.__POLARITY_KEY]
        if self.__OVERLOADING_STATE_KEY in kwargs:
            self._overloading = kwargs[self.__OVERLOADING_STATE_KEY]

    def get_powering_state(self):
        return self._powering_state

    def is_overloading_present(self):
        """
           Checking if HV has capabilities to control overloading (visual indication)
        :return: True if overloading control present
        """
        return self._overloading is not None

    def get_overload_state(self):
        return self._overloading

    def is_voltage_present(self):
        """
           Checking if HV has capabilities to show voltage value (visual indication)
        :return:
        """
        return self._voltage_value is not None

    def get_voltage(self):
        raise self._voltage_value

    def is_polarity_present(self):
        """
           Checking if HV has capabilities to control polarity of hv (visual indication)
        :return:
        """
        return self._polarity is not None

    def get_polarity(self):
        """
           Check if polarity control present
        :return:
        """
        raise self._polarity is not None

    __NEGATIVE_POLARITY = 1
    __POSITIVE_POLARITY = 2
    __HV_TYPE_KEY = u'HV_TYPE'
    __POWERING_STATE_KEY = u'POWERING_STATE'
    __OVERLOADING_STATE_KEY = u'OVERLOADING_STATE'
    __VOLTAGE_KEY = u'VOLTAGE'
    __POLARITY_KEY = u'POLARITY'

    _hv_type = u''
    _powering_state = False
    _polarity = None
    _overloading = False
    _voltage_value = None
