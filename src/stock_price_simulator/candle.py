
class Candle:
    def __init__(self, open: float, close: float, high: float, low: float, volume: float):
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.volume = volume

    def display(self):
        print(f"Open: {self.open}, Close: {self.close}, High: {self.high}, Low: {self.low}, Volume: {self.volume}")

    def spread(self) -> float:
        return self.high - self.low
    
    def edit(self, open: float = None, close: float = None, high: float = None, low: float = None, volume: float = None):
        self.open = open if open is not None else self.open
        self.close = close if close is not None else self.close
        self.high = high if high is not None else self.high
        self.low = low if low is not None else self.low
        self.volume = volume if volume is not None else self.volume
