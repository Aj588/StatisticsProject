import unittest

from Calculator.Calculator import


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
        self.statistics = Statistics()

    def test_calculator_return_sum(self):
        calculator = Calculator()
        result = calculator.Sum(1, 2)
        self.assertEqual(3, result)