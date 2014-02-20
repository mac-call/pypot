import numpy

import pypot.primitive


class Sinus(pypot.primitive.LoopPrimitive):
    """ Apply a sinus on the motor specified as argument. Parameters (amp, offset and phase) should be specified in degree
    """
    def __init__(self, robot, refresh_freq,
                 motor_list,
                 amp=1, freq=0.5, offset=0, phase=0):

        pypot.primitive.LoopPrimitive.__init__(self, robot, refresh_freq,
                                               amp, freq, offset, phase)

        self.freq = freq
        self.amp = amp
        self.offset = offset
        self.phase = phase

        self.motor_list = [self.get_mockup_motor(m) for m in motor_list]

    def update(self):
        """ Compute the sin(t) where t is the elapsed time since the primitive has been started. """
        pos = self.amp * numpy.sin(self.freq * 2.0 * numpy.pi * self.elapsed_time +
                              self.phase * numpy.pi / 180.0) + self.offset

        for m in self.motor_list:
            m.goal_position = pos

    @property
    def frequency(self):
        return self.freq

    @frequency.setter
    def frequency(self, new_freq):
        self.freq = new_freq

    @property
    def amplitude(self):
        return self.amp

    @amplitude.setter
    def amplitude(self, new_amp):
        self.amp = new_amp

    @property
    def offset(self):
        return self.offset

    @offset.setter
    def offset(self, new_offset):
        self.offset = new_offset

    @property
    def phase(self):
        return self.phase

    @phase.setter
    def phase(self, new_phase):
        self.phase = new_phase


class Cosinus(Sinus):
    """ Apply a cosinus on the motor specified as argument. Parameters (amp, offset and phase) should be specified in degree
    """
    def __init__(self, robot, refresh_freq,
                 motor_list,
                 amp=1, freq=0.5, offset=0, phase=0):

        Sinus.__init__(self, robot, refresh_freq,
                       motor_list,
                       amp, freq, offset, phase=(numpy.pi / 2 + phase))

