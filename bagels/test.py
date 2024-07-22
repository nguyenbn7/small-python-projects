import unittest

from __init__ import NUM_DIGITS, getSecretNum


class TestFunctions(unittest.TestCase):

    def test_get_secret_number_random_and_len_equals_to_NUM_DIGITS(self):
        first_num = getSecretNum()
        second_num = getSecretNum()

        self.assertEqual(len(first_num), NUM_DIGITS)
        self.assertNotEqual(first_num, second_num)
