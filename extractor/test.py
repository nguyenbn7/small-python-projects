import unittest

from __init__ import phone_pattern


class TestPhoneRegex(unittest.TestCase):

    def test_1(self):
        given = "(212)-456-7890"

        match_obj = phone_pattern.match(given)

        self.assertIsNotNone(match_obj)
        self.assertEqual(match_obj.group(2), "(212)")
        self.assertEqual(match_obj.group(3), "-")
        self.assertEqual(match_obj.group(4), "456")
        self.assertEqual(match_obj.group(5), "-")
        self.assertEqual(match_obj.group(6), "7890")
