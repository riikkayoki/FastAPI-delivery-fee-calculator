import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_small_order_fee_cart_value_under_1000(self):
        self.calculator = Calculator(1, 0, 0, 0)
        self.calculator.get_small_order_fee()
        self.assertEqual(self.calculator.delivery_fee, 999)

    def test_small_order_fee_cart_value_over_1000(self):
        self.calculator = Calculator(1200, 0, 0, 0)
        self.calculator.get_small_order_fee()
        self.assertEqual(self.calculator.delivery_fee, 0)

    def test_delivery_fee_when_distance_first_500_km(self):
        self.calculator = Calculator(0, 450, 0, 0)
        self.calculator.get_delivery_fee_by_distance()
        self.assertEqual(self.calculator.delivery_fee, 10)

        self.calculator = Calculator(0, 500, 0, 0)
        self.calculator.get_delivery_fee_by_distance()
        self.assertEqual(self.calculator.delivery_fee, 10)

    def test_delivery_fee_when_distance_between_500_1000_km(self):
        self.calculator = Calculator(0, 900, 0, 0)
        self.calculator.get_delivery_fee_by_distance()
        self.assertEqual(self.calculator.delivery_fee, 20)

    def test_delivery_fee_when_distance_1000_km(self):
        self.calculator = Calculator(0, 1000, 0, 0)
        self.calculator.get_delivery_fee_by_distance()
        self.assertEqual(self.calculator.delivery_fee, 20)

    def test_delivery_fee_when_distance_under_1501_km(self):
        self.calculator = Calculator(1, 1500, 1, 1)
        self.calculator.get_delivery_fee_by_distance()
        self.assertEqual(self.calculator.delivery_fee, 20)

    def test_delivery_fee_when_distance_over_1500(self):
        self.calculator = Calculator(0, 1501, 0, 0)
        self.calculator.get_delivery_fee_by_distance()
        self.assertEqual(self.calculator.delivery_fee, 30)

        self.calculator = Calculator(0, 23456, 0, 0)
        self.calculator.get_delivery_fee_by_distance()
        self.assertEqual(self.calculator.delivery_fee, 460)

    def test_delivery_fee_under_4_items(self):
        self.calculator = Calculator(0, 0, 4, 0)
        self.calculator.get_extra_fee_if_over_four_items()
        self.assertEqual(self.calculator.delivery_fee, 0)

    def test_delivery_fee_5_items(self):
        self.calculator = Calculator(0, 0, 5, 0)
        self.calculator.get_extra_fee_if_over_four_items()
        self.assertEqual(self.calculator.delivery_fee, 5)

    def test_delivery_fee_10_items(self):
        self.calculator = Calculator(0, 0, 10, 0)
        self.calculator.get_extra_fee_if_over_four_items()
        self.assertEqual(self.calculator.delivery_fee, 30)

    def test_free_delivery_if_cart_value_1000_or_more(self):
        self.calculator = Calculator(1000, 0, 0, 0)
        self.calculator.get_free_delivery()
        self.assertEqual(self.calculator.delivery_fee, 0)
