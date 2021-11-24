import unittest
from main import verify_email

class TestVerifyEmail(unittest.TestCase):

    def test_invalid_emails(self):
        invalidEmails = [
            'abc-@mail.com',
            'abc..def@mail.com',
            '.abc@mail.com',
            'abc#def@mail.com',
            'abc.def@mail.c',
            'abc.def@mail#archive.com',
            'abc.def@mail',
            'abc.def@mail..com'
        ]

        for invalidEmail in invalidEmails:
            self.assertFalse(verify_email(invalidEmail))

    def test_valid_emails(self):
        validEmails = [
            'abc-d@mail.com',
            'abc.def@mail.com',
            'abc@mail.com',
            'abc_def@mail.com',
            'abc.def@mail.cc',
            'abc.def@mail-archive.com',
            'abc.def@mail.org',
            'abc.def@mail.com'
        ]

        for validEmail in validEmails:
            self.assertTrue(verify_email(validEmail))

