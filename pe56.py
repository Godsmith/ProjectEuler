import unittest
from itertools import product

from integer_functions import digit_list


class TestDigitalSum(unittest.TestCase):
    def test_simple(self):
        self.assertEquals(digital_sum(123), 6)

    def test_other(self):
        self.assertEquals(digital_sum(999), 27)

    def test_single_digit(self):
        self.assertEquals(digital_sum(9), 9)


def digital_sum(i):
    return sum(digit_list(i))


print(max([digital_sum(a ** b) for a, b in product(range(1, 101), range(1, 101))]))
