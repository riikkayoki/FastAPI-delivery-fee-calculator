import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_small_order_fee_cart_value_under_1000(self):
        self.calculator = Calculator(1, 1, 1, 10)
        self.calculator.get_small_order_fee()
        self.assertEqual(self.calculator.delivery_fee, 999)

    def test_small_order_fee_cart_value_over_1000(self):
        self.calculator = Calculator(1200, 1, 1, 10)
        self.calculator.get_small_order_fee()
        self.assertEqual(self.calculator.delivery_fee, 0)

    def test_delivery_fee_when_distance_first_500_km(self):
        self.calculator = Calculator(6000, 450, 1, 1)
        self.calculator.get_delivery_fee_by_distance()
        self.assertEqual(self.calculator.delivery_fee, 10)

        self.calculator = Calculator(6000, 500, 1, 1)
        self.calculator.get_delivery_fee_by_distance()
        self.assertEqual(self.calculator.delivery_fee, 10)

    def test_delivery_fee_when_distance_between_500_1000_km(self):
        self.calculator = Calculator(5000, 900, 1, 1)
        self.calculator.get_delivery_fee_by_distance()
        self.assertEqual(self.calculator.delivery_fee, 20)

    def test_delivery_fee_when_distance_1000_km(self):
        self.calculator = Calculator(5000, 1000, 1, 1)
        self.calculator.get_delivery_fee_by_distance()
        self.assertEqual(self.calculator.delivery_fee, 20)

    def test_delivery_fee_when_distance_under_1501_km(self):
        self.calculator = Calculator(5000, 1500, 1, 1)
        self.calculator.get_delivery_fee_by_distance()
        self.assertEqual(self.calculator.delivery_fee, 20)

    def test_delivery_fee_when_distance_over_1500(self):
        self.calculator = Calculator(5000, 1501, 1, 1)
        self.calculator.get_delivery_fee_by_distance()
        self.assertEqual(self.calculator.delivery_fee, 30)

        self.calculator = Calculator(5000, 23456, 1, 1)
        self.calculator.get_delivery_fee_by_distance()
        self.assertEqual(self.calculator.delivery_fee, 460)

