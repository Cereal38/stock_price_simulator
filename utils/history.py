
import matplotlib.pyplot as plt
import random as rd

from utils.candle import Candle

class History:
    def __init__ (self, candles=[]):
        self.candles = candles

    def display(self):
        plt.plot([candle.close for candle in self.candles])
        plt.show()

    def generateHistory(self, initPrice: float, duration: int):
        """
        initPrice: float
        duration: int (in minutes)
        """
        
        # Generate a random history
        self.candles = []
        price = initPrice
        for i in range(duration):
            price = price + rd.normalvariate(0, 2)
            candle = Candle(price, price, price, price, 1)
            self.candles.append(candle)