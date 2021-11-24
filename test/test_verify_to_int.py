import unittest
from main import toInt

class TestVerifyToInt(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(toInt('1245') + 1, 1246)
        self.assertEqual(toInt('312') + 5, 317)
        self.assertEqual(toInt('21') - 1, 20)



