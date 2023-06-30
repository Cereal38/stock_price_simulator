
import random as rd
import matplotlib.pyplot as plt
import math
import numpy as np

# import my file maths.py
import maths

DURATION = 365 * 24 * 60 # In minutes
INIT_PRICE = 100

def nextCandle(current_price, moving_average=0):
    """
    Generate next candle based on current price and the difference between current price and moving average
    :param current_price: current price
    :param moving_average: moving average
    :return: next candle
    """
    # Generate a random number using normal distribution
    x = rd.normalvariate(0, 1)
    # Generate next candle
    if moving_average == 0:
      next_candle = current_price + x
    else:
      next_candle = current_price + (moving_average - current_price) / 1000 + x 
    return next_candle

def generateChart(current_price, duration):
    """
    Generate chart
    :param current_price: current price
    :param duration: duration of the simulation
    :return: list of candles
    """
    candles = [INIT_PRICE]
    for i in range(duration):
        current_price = nextCandle(current_price, maths.movingAverage(candles, 15 * 24 * 60))
        candles.append(current_price)
    return candles

def main():
    candles = generateChart(INIT_PRICE, DURATION)
    moving_average = maths.movingAverage(candles, 15 * 24 * 60)

    plt.plot(candles, label='Candles')
    plt.plot(moving_average, label='Moving average')
    plt.show()

if __name__ == '__main__':
    main()