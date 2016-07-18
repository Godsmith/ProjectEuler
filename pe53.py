from math import factorial
from unittest import TestCase


class TestSelectRFromN(TestCase):
    def test_3_5(self):
        self.assertEquals(select_r_from_n(3, 5), 10)

    def test_10_23(self):
        self.assertEquals(select_r_from_n(10, 23), 1144066)


def select_r_from_n(r, n):
    return factorial(n) / (factorial(r) * factorial(n - r))


count = 0
for n in range(1, 101):
    for r in range(1, n + 1):
        if select_r_from_n(r, n) > 1000000:
            count += 1
print(count)
