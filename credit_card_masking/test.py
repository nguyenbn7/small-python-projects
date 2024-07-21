import unittest

from credit_card_masking.main import mask_credit_card


class TestMaskingCreditCard(unittest.TestCase):

    def test_1(self):
        given = "1111222233334444"
        expected = f"1111{'*' * 8}4444"

        actual = mask_credit_card(given, True)
        self.assertEqual(expected, actual)

    def test_2(self):
        given = "1111 2222 3333 4444"
        expected = f"1111{'*' * 8}4444"

        actual = mask_credit_card(given, True)
        self.assertEqual(expected, actual)

    def test_3(self):
        given = "1111-2222-3333-4444"
        expected = f"1111{'*' * 8}4444"

        actual = mask_credit_card(given, True)
        self.assertEqual(expected, actual)
