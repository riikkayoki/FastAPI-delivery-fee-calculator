import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(1, 1, 1, 10)

    def test_calculator(self):
        pass
