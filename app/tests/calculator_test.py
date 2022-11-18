import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(1, 1, 1, 10)

    def test_small_order_fee(self):
        self.calculator.cart_value = 11
        self.assertTrue(self.calculator.get_small_order_fee())

        self.calculator.cart_value = 1100
        self.assertFalse(self.calculator.get_small_order_fee())

    