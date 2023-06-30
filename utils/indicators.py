
import random as rd
import matplotlib.pyplot as plt
import math
import numpy as np

# Generate a random number using normal distribution
# x = rd.normalvariate(13, 5)


def movingAverage(data, window_size):
    """
    Compute moving average
    :param data: list of numbers
    :param window_size: size of the window (in number of elements)
    :return: list of moving average
    """
    
    kernel = np.ones(window_size) / window_size
    moving_average = np.convolve(data, kernel, 'valid')
    return moving_average