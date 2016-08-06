import unittest

from pe60 import all_possible_concatenations_of_two, combinations_in_sum_order, combinations_of_pair_are_primes, \
    pairs_from_list
from primes import primes_up_to


class TestAllPossibleConcatenationsOfTwo(unittest.TestCase):
    def test_easy(self):
        self.assertEquals(all_possible_concatenations_of_two([1, 2, 3]), [12, 21, 13, 31, 23, 32])


class TestSortedCombinations(unittest.TestCase):
    def test_length_1_r_1(self):
        self.assertEquals(list(combinations_in_sum_order([1], 1)), [[1]])

    def test_length_2_r_2(self):
        self.assertEquals(list(combinations_in_sum_order([1, 2], 2)), [[1, 2]])

    def test_length_2_r_1(self):
        self.assertEquals(list(combinations_in_sum_order([1, 2], 1)), [[1], [2]])

    def test_length_3_r_2(self):
        self.assertEquals(list(combinations_in_sum_order([1, 2, 3], 2)), [[1, 2], [1, 3], [2, 3]])

    def test_length_4_r_2(self):
        self.assertEquals(list(combinations_in_sum_order([1, 2, 3, 10], 2)), [[1, 2], [1, 3], [2, 3],
                                                                              [1, 10], [2, 10], [3, 10]])

    def test_length_4_r_3(self):
        self.assertEquals(list(combinations_in_sum_order([1, 2, 3, 10], 3)), [[1, 2, 3], [1, 2, 10], [1, 3, 10],
                                                                              [2, 3, 10]])


class TestCombinationOfPairArePrimes(unittest.TestCase):
    def test_true(self):
        self.assertEquals(True, combinations_of_pair_are_primes((3, 7), primes_up_to(100)))

    def test_false(self):
        self.assertEquals(False, combinations_of_pair_are_primes((3, 5), primes_up_to(100)))


class TestPairsFromList(unittest.TestCase):
    def test_simple(self):
        self.assertEquals([(1, 2), (1, 3), (2, 3)], pairs_from_list([1, 2, 3]))
