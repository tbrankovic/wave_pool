import numpy as np
from tbrankovic.utils.plot_graph import plot_graph


def pulse_shape(periods, taps, filter='square'):
    # make filter name lowercase
    filter = filter.lower()

    # set filter period and size
    Ts = periods
    t = np.arange(taps) - (taps - 1) // 2

    # set h = 0 in case of error with filter parameter
    h = np.zeros_like(t)

    # square filter
    if filter == 'square':
        h = np.where(np.abs(t) <= periods / 2, 1, 0)

    # raised cosine filter
    if filter == 'raised cosine':
        beta = 0.35
        h = 1 / Ts * np.sinc(t / Ts) * np.cos(np.pi * beta * t / Ts) / (1 - (2 * beta * t / Ts) ** 2)

    return t, h

# pulse_shape(10, 201, filter="square")