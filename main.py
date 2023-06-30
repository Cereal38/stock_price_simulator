
import random as rd
import math
import numpy as np

import maths
from utils.candle import Candle
from utils.history import History

DURATION = 365 * 24 * 60 # In minutes
INIT_PRICE = 100
rules = [{
    "condition": lambda history: True,
    "action": lambda history: history.candles[-1].edit(
        close = history.candles[-1].close * rd.normalvariate(1.001, 0.01)
    )
}]


def main():
    
    # Generate a random history
    history = History()
    history.generateHistory(
        INIT_PRICE, 
        DURATION,
        rules
    )
    history.display()

if __name__ == '__main__':
    main()