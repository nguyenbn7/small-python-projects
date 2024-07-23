import unittest

from functions import calculate


# TODO: add more tests
class TestCalculator(unittest.TestCase):

    def test_1(self):
        expression = "3 * 4 + 2"
        expected = 14

        actual = calculate(expression)

        self.assertEqual(expected, actual)

    def test_2(self):
        expression = "3 ^ 3 / 2"
        expected = 13.5

        actual = calculate(expression)

        self.assertEqual(expected, actual)
