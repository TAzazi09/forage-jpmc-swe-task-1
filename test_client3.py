import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
    
    def test_getDataPoint(self):
        # Arrange
        quote = {
            'stock': 'ABC',
            'top_bid': {'price': 120.48, 'size': 10},
            'top_ask': {'price': 121.2, 'size': 15}
        }
        expected_stock = 'ABC'
        expected_bid_price = 120.48
        expected_ask_price = 121.2
        expected_price = (expected_bid_price + expected_ask_price) / 2

        # Act
        stock, bid_price, ask_price, price = getDataPoint(quote)

        # Assert
        self.assertEqual(stock, expected_stock)
        self.assertEqual(bid_price, expected_bid_price)
        self.assertEqual(ask_price, expected_ask_price)
        self.assertEqual(price, expected_price)

    def test_getRatio(self):
        # Arrange
        price_a = 120.48
        price_b = 121.2
        expected_ratio = price_a / price_b

        # Act
        ratio = getRatio(price_a, price_b)

        # Assert
        self.assertEqual(ratio, expected_ratio)

    def test_getRatio_price_b_zero(self):
        # Arrange
        price_a = 120.48
        price_b = 0
        expected_ratio = None  # or you can use float('inf') or any expected result you defined for division by zero

        # Act
        ratio = getRatio(price_a, price_b)

        # Assert
        self.assertIsNone(ratio)

if __name__ == '__main__':
    unittest.main()
