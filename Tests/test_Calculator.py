import unittest

from Calculator.Calculator import Calculator
from MathOperations.division import Division
from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()


    def test_calculator_return_sum(self):
        self.assertEqual(3, Addition.sum(1,2))

    def test_calculator_return_difference(self):
        self.assertEqual(-1, Subtraction.difference(1,2))

    def test_calculator_return_fraction(self):
        self.assertEqual(5, Division.fraction(10,2))

if __name__ == '__main__':
    unittest.main()