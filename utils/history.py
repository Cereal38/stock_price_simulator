
import matplotlib.pyplot as plt
import numpy as np
import mplfinance as mpf
import pandas as pd

from utils.candle import Candle

class History:
    def __init__ (self, candles: list = []):
        self.candles = candles
        self.length = len(candles)

    def addCandle(self, candle: Candle):
        self.candles.append(candle)
        self.length += 1


    def display(self):

        # Plot candles as a candlestick chart
        # Add indicators
        df = pd.DataFrame({
            "Open": [candle.open for candle in self.candles],
            "Close": [candle.close for candle in self.candles],
            "High": [candle.high for candle in self.candles],
            "Low": [candle.low for candle in self.candles],
            "Volume": [candle.volume for candle in self.candles],
        })
        df.index = pd.to_datetime(df.index, unit='m')
        df = df.iloc[::-1]
        mpf.plot(df, type='candle', style='charles', volume=True, warn_too_much_data=20000)
            

    def generateHistory(self, initPrice: float = 100, duration: int = 24*60, rules: list = []):
        """
        initPrice: float
        duration: int (in minutes)
        rules: list of objects
          Each object contains a condition (as lambda function) and an action (as lambda function)
          The condition is a function that takes history as argument and returns a boolean
          The action is a function that takes history as argument and modifies it
        """

        # Generate the first candle
        self.addCandle(Candle(initPrice, initPrice, initPrice, initPrice, 0))

        # Generate the following candles
        for i in range(1, duration):
            
            # Duplicate the previous candle
            self.addCandle(Candle(
                self.candles[-1].open,
                self.candles[-1].close,
                self.candles[-1].high,
                self.candles[-1].low,
                self.candles[-1].volume
            ))

            # Apply the rules
            for rule in rules:
                if rule["condition"](self):
                    rule["action"](self)
