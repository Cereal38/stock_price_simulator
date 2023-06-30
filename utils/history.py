
import matplotlib.pyplot as plt

class History:
    def __init__ (self, candles: list):
        self.candles = candles

    def display(self):
        plt.plot([candle.close for candle in self.candles])
        plt.show()