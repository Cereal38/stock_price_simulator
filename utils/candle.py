
class Candle:
    def __init__(self, open: float, close: float, high: float, low: float, volume: float):
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.volume = volume

    def spread(self) -> float:
        return self.high - self.low
