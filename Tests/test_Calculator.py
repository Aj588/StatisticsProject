import unittest

from Calculator.Calculator import


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

if __name__ == '__main__':
    unittest.main()