''' Unit test for Calculator.py application'''
import unittest

from Calc import Calculator


class TestCalculator(unittest.TestCase):

    def test_Calculator(self):
        calculator = Calculator()
        output = {'sum': 7}
        input = {'num1': 2, 'num2': 5}
        result = calculator.post(input)
        self.assertEqual(output, result)

    def test_Calculator_with_strings(self):
        calculator = Calculator()
        output = {'sum': '52'}
        input = {'num1': "5", 'num2': "2"}
        result = calculator.post(input)
        self.assertEqual(output, result)

    def test_Calculator_with_float(self):
        calculator = Calculator()
        output = {'sum': 7}
        input = {'num1': 3.5, 'num2': 3.5}
        result = calculator.post(input)
        self.assertEqual(output, result)

    def test_Calculator_with_null(self):
        calculator = Calculator()
        output = {'sum': 7}
        input = {'num1': None, 'num2': None}
        result = calculator.post(input)
        self.assertEqual(output, result)


if __name__ == "__main__":
    unittest.main()
