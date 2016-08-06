import unittest

import primes


class TestPrimesUpTo(unittest.TestCase):
    def test_10(self):
        self.assertEquals([2, 3, 5, 7], primes.primes_up_to(10))


class TestIsPrime(unittest.TestCase):
    def test_7_then_19(self):
        self.assertEquals(True, primes.is_prime(7))
        self.assertEquals(True, primes.is_prime(19))
