
import unittest


import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.stock_price_simulator.candle import Candle


class TestCandle(unittest.TestCase):
    def setUp(self):
        self.candle = Candle(1.0, 2.0, 3.0, 0.5, 100.0)

    def test_init(self):
        self.assertEqual(self.candle.open, 1.0)
        self.assertEqual(self.candle.close, 2.0)
        self.assertEqual(self.candle.high, 3.0)
        self.assertEqual(self.candle.low, 0.5)
        self.assertEqual(self.candle.volume, 100.0)

    def test_spread(self):
        self.assertEqual(self.candle.spread(), 2.5)  # 3.0 - 0.5

    def test_edit(self):
        self.candle.edit(open=1.5, close=2.5)
        self.assertEqual(self.candle.open, 1.5)
        self.assertEqual(self.candle.close, 2.5)
        # Check that the other attributes are not changed
        self.assertEqual(self.candle.high, 3.0)
        self.assertEqual(self.candle.low, 0.5)
        self.assertEqual(self.candle.volume, 100.0)

if __name__ == '__main__':
    unittest.main()
