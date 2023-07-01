
import random as rd
import math
import numpy as np

from utils.indicators import movingAverage
from utils.candle import Candle
from utils.history import History

DURATION = 365 * 24 * 60 # In minutes
INIT_PRICE = 100
rules = [{
    "condition": lambda history: history.candles[-1].close > INIT_PRICE,
    "action": lambda history: history.candles[-1].edit(
        close = history.candles[-1].close + rd.normalvariate(-0.001, 0.5),
    )
},
{
    "condition": lambda history: history.candles[-1].close < INIT_PRICE,
    "action": lambda history: history.candles[-1].edit(
        close = history.candles[-1].close + rd.normalvariate(0.001, 0.5),
    )
},
{
    "condition": lambda history: history.candles[-1].close == INIT_PRICE,
    "action": lambda history: history.candles[-1].edit(
        close = history.candles[-1].close + rd.normalvariate(0, 0.5),
    )
},
{
    "condition": lambda history: history.candles[-1].close / INIT_PRICE < 0.5,
    "action": lambda history: history.candles[-1].edit(
        close = history.candles[-1].close + rd.normalvariate(1 - history.candles[-1].close / INIT_PRICE, 0.5),
    )
},
{
    "condition": lambda history: history.length > 1,
    "action": lambda history: history.candles[-1].edit(
        open = history.candles[-2].close,
        low = min(history.candles[-1].open, history.candles[-1].close) + max(rd.uniform(-0.4, 0.1), 0),
        high = max(history.candles[-1].open, history.candles[-1].close) + min(rd.uniform(-0.1, 0.4), 0),
    )
}]


def main():

    history = History()
    history.randomWalk(INIT_PRICE, DURATION, 0.1)
    history.display("d")

if __name__ == '__main__':
    main()