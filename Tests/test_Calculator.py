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

    def test_calculator_access_difference_result(self):
        calculator = Calculator()
        calculator.Difference(1, 2)
        self.assertEqual(-1, calculator.Result)

    def test_calculator_access_sum_result(self):
        calculator = Calculator()
        calculator.Sum(1, 2)
        self.assertEqual(3, calculator.Result)

    def test_calculator_access_fraction_result(self):
        calculator = Calculator()
        calculator.Fraction(5, 5)
        self.assertEqual(1, calculator.Result)



if __name__ == '__main__':
    unittest.main()