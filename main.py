
import random as rd
import matplotlib.pyplot as plt
import math
import numpy as np

import maths
from utils.candle import Candle
from utils.history import History

DURATION = 365 * 24 * 60 # In minutes
INIT_PRICE = 100


def main():
    
    # Generate a random history
    candles = []
    price = INIT_PRICE
    for i in range(DURATION):
        price = price + rd.normalvariate(0, 2)
        candles.append(Candle(price, price, price, price, 1))
    history = History(candles)
    history.display()

if __name__ == '__main__':
    main()