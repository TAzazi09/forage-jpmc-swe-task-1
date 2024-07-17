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
        expected_data_point = ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2)
        
        # Act
        data_point = getDataPoint(quote)
        
        # Assert
        self.assertEqual(data_point, expected_data_point)
    
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
        expected_ratio = None  # Since dividing by zero is undefined, we expect None or you can define any behavior.
        
        # Act
        ratio = getRatio(price_a, price_b)
        
        # Assert
        self.assertIsNone(ratio)

if __name__ == '__main__':
    unittest.main()
