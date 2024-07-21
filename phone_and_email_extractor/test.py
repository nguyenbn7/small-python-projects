import re
import unittest
from phone_and_email_extractor.main import phone_regex_pattern


class TestPhoneRegex(unittest.TestCase):

    def test_(self):
        given = "(212)-456-7890"

        match_obj = re.match(phone_regex_pattern, given)

        self.assertIsNotNone(match_obj)
        self.assertEqual(match_obj.group(2), "(212)")
        self.assertEqual(match_obj.group(3), "-")
        self.assertEqual(match_obj.group(4), "456")
        self.assertEqual(match_obj.group(5), "-")
        self.assertEqual(match_obj.group(6), "7890")
