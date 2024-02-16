import numpy as np


def generate_waveform(pulse_shape, binary_stream):
    # y = np.convolve(pulse_shape, binary_stream)
    y = []
    for b in binary_stream:
        y = np.concatenate((y, pulse_shape * b))

    # generate x-axis values based on length of y
    x = np.arange(len(y))

    return x, y