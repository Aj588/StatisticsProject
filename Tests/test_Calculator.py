import unittest

from Calculator.Calculator import Calculator
import unittest

from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()


    def test_calculator_return_sum(self):
        calculator = Calculator()
        result = calculator.Sum(1, 2)
        self.assertEqual(3, result)

    def test_calculator_return_difference(self):
        calculator = Calculator()
        result = calculator.Difference(1, 2)
        self.assertEqual(-1, result)

    def test_calculator_return_fraction(self):
        calculator = Calculator()
        result = calculator.Fraction(10,2)
        self.assertEqual(5, result)

if __name__ == '__main__':
    unittest.main()