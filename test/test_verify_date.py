import unittest
from main import verify_date

class TestVerifyDate(unittest.TestCase):

    def test_invalid_dates(self):
        invalidDates = [
            'qwcascasc',
            '12/qw/1455',
            '///',
            '//'
        ]

        for invalidDate in invalidDates:
            self.assertFalse(verify_date(invalidDate))

    def test_valid_dates(self):
        validDates = [
            '12/12/12',
            '20/11/12',
            '20/12/21',
            '30/01/19'
        ]

        for validDate in validDates:
            self.assertTrue(verify_date(validDate))

