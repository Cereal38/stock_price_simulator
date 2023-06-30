
import random as rd
import math
import numpy as np

import maths
from utils.candle import Candle
from utils.history import History

DURATION = 365 * 24 * 60 # In minutes
INIT_PRICE = 100


def main():
    
    # Generate a random history
    history = History()
    history.generateHistory(INIT_PRICE, DURATION)
    history.display()

if __name__ == '__main__':
    main()