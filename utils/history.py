
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

from utils.candle import Candle

class History:
    def __init__ (self, candles: list = []):
        self.candles = candles
        self.length = len(candles)

    def addCandle(self, candle: Candle):
        self.candles.append(candle)
        self.length += 1


    def display(self, indicators: list = []):
        """
        indicators: list of functions
          Each function takes history as argument and returns a list of values
        """

        # Plot the candles
        # plt.plot([candle.close for candle in self.candles])

        # Plot candles as a candlestick chart
        fig = go.Figure(data=[go.Candlestick(x=np.arange(len(self.candles)),
            open=[candle.open for candle in self.candles],
            high=[candle.high for candle in self.candles],
            low=[candle.low for candle in self.candles],
            close=[candle.close for candle in self.candles])])
        fig.show()
        
      

        # Plot the indicators
        # for indicator in indicators:
        #     plt.plot(indicator(self))

        # plt.show()

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
