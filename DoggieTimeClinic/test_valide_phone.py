import unittest
from active import is_valid_phone
class Phone_true_Test(unittest.TestCase):
    def test_is_match1(self):
        self.assertTrue(is_valid_phone("89319916462"))

    def test_is_match2(self):
        self.assertTrue(is_valid_phone("8 931991-64-62"))

    def test_is_match3(self):
        self.assertTrue(is_valid_phone("+7 931 99164-62"))

    def test_is_match4(self):
        self.assertTrue(is_valid_phone("84739574929"))

    def test_is_match5(self):
        self.assertTrue(is_valid_phone("+7 565677 67-67"))

    def test_is_match6(self):
        self.assertTrue(is_valid_phone("+7 (565)677 67-67"))

    def test_is_match7(self):
        self.assertTrue(is_valid_phone("+7(565) 677 67-67"))

class Phone_false_Test(unittest.TestCase):
    def test_is_not_match1(self):
        self.assertFalse(is_valid_phone("9 931991-64-62"))

    def test_is_not_match2(self):
        self.assertFalse(is_valid_phone("+8-931 99164-62"))

    def test_is_not_match3(self):
        self.assertFalse(is_valid_phone("84 739574929"))

    def test_is_not_match4(self):
        self.assertFalse(is_valid_phone("+7 565_-677 67-67"))

    def test_is_not_match5(self):
        self.assertFalse(is_valid_phone("+7 ( 565 677 67-67"))
