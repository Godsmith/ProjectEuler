import unittest

from pe55 import reverse_integer, is_palindrome


class TestReverseInteger(unittest.TestCase):
    def test_two_digits(self):
        self.assertEquals(reverse_integer(47), 74)

    def test_two_different_digits(self):
        self.assertEquals(reverse_integer(38), 83)

    def test_three_digits(self):
        self.assertEquals(reverse_integer(349), 943)

    def test_four_digits(self):
        self.assertEquals(reverse_integer(1292), 2921)


class TestIsPalindromeInteger(unittest.TestCase):
    def test_is_not_palindrome(self):
        self.assertFalse(is_palindrome(1292))

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(12921))
