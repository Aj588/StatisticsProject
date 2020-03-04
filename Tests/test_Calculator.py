import unittest
from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()


    def test_calculator_return_sum(self):
        calculator = Calculator()
        result = calculator.sum(1, 2)
        self.assertEqual(result, 3)

    def test_calculator_return_difference(self):
        calculator = Calculator()
        result = calculator.difference(1, 2)
        self.assertEqual(result, -1)

    def test_calculator_access_difference_result(self):
        calculator = Calculator()
        calculator.difference(1, 2)
        self.assertEqual(calculator.Result, -1)

    def test_calculator_access_sum_result(self):
        calculator = Calculator()
        calculator.sum(1, 2)
        self.assertEqual(calculator.Result, 3)

    def test_calculator_access_fraction_result(self):
        calculator = Calculator()
        calculator.fraction(5, 5)
        self.assertEqual(calculator.Result, 1)

if __name__ == '__main__':
    unittest.main()