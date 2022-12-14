import unittest
from datetime import datetime
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.friday_is_rush = datetime.fromisoformat(
            "2022-11-25T15:00:00+00:01")
        self.not_friday_but_rush_hour = datetime.fromisoformat(
            "2022-11-24T12:15:00+00:00")
        self.friday_is_not_rush = datetime.fromisoformat(
            "2022-11-25T12:00:00+00:00")

    def test_small_order_fee_cart_value_under_1000(self):
        self.calculator = Calculator(1, 0, 0, 0)
        self.calculator.get_small_order_fee()
        self.assertEqual(self.calculator.delivery_fee, 1199)

    def test_small_order_fee_cart_value_over_1000(self):
        self.calculator = Calculator(1200, 0, 0, 0)
        self.calculator.get_small_order_fee()
        self.assertEqual(self.calculator.delivery_fee, 200)

    def test_delivery_fee_when_distance_first_1000_km(self):
        self.calculator = Calculator(0, 1000, 0, 0)
        self.calculator.get_delivery_fee_by_distance()
        self.assertEqual(self.calculator.delivery_fee, 200)

    def test_delivery_fee_when_distance_under_1501_km(self):
        self.calculator = Calculator(1, 1500, 1, 1)
        self.calculator.get_delivery_fee_by_distance()
        self.assertEqual(self.calculator.delivery_fee, 300)

    def test_delivery_fee_when_distance_over_1500(self):
        self.calculator = Calculator(0, 1501, 0, 0)
        self.calculator.get_delivery_fee_by_distance()
        self.assertEqual(self.calculator.delivery_fee, 400)

        self.calculator = Calculator(0, 23456, 0, 0)
        self.calculator.get_delivery_fee_by_distance()
        self.assertEqual(self.calculator.delivery_fee, 4700)

    def test_delivery_fee_under_4_items(self):
        self.calculator = Calculator(0, 0, 4, 0)
        self.calculator.get_extra_fee_if_over_four_items()
        self.assertEqual(self.calculator.delivery_fee, 200)

    def test_delivery_fee_5_items(self):
        self.calculator = Calculator(0, 0, 5, 0)
        self.calculator.get_extra_fee_if_over_four_items()
        self.assertEqual(self.calculator.delivery_fee, 205)

    def test_delivery_fee_10_items(self):
        self.calculator = Calculator(0, 0, 10, 0)
        self.calculator.get_extra_fee_if_over_four_items()
        self.assertEqual(self.calculator.delivery_fee, 230)

    def test_free_delivery_if_cart_value_1000_or_more(self):
        self.calculator = Calculator(1001, 0, 0, 0)
        self.calculator.get_free_delivery()
        self.assertEqual(self.calculator.delivery_fee, 0)

    def test_free_delivery_if_cart_value_under_1000(self):
        self.calculator = Calculator(900, 0, 0, 0)
        self.calculator.get_free_delivery()
        self.assertEqual(self.calculator.delivery_fee, 200)

    def test_rush_hour_fee_when_rush_hour(self):
        self.calculator = Calculator(0, 0, 0, self.friday_is_rush)
        self.calculator.get_friday_rush_hour_fee()
        self.assertEqual(self.calculator.delivery_fee, 220)

    def test_rush_hour_fee_when_friday_but_not_rush_hour(self):
        self.calculator = Calculator(0, 0, 0, self.friday_is_not_rush)
        self.calculator.get_friday_rush_hour_fee()
        self.assertEqual(self.calculator.delivery_fee, 200)

    def test_rush_hour_fee_when_not_friday_but_is_rush_hour(self):
        self.calculator = Calculator(0, 0, 0, self.not_friday_but_rush_hour)
        self.calculator.get_friday_rush_hour_fee()
        self.assertEqual(self.calculator.delivery_fee, 200)

    def test_maximum_delivery_fee(self):
        self.calculator = Calculator(50, 3000, 100, self.friday_is_rush)
        self.calculator.get_total_delivery_fee()
        self.assertEqual(self.calculator.delivery_fee, 1500)

    def test_total_fee_under_maximum_delivery_fee(self):
        self.calculator = Calculator(100, 1000, 4, self.friday_is_rush)
        self.calculator.get_total_delivery_fee()
        self.assertEqual(self.calculator.delivery_fee, 1210)
