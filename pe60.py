import unittest
from itertools import combinations
from itertools import chain
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


def is_prime_in_concatenation_of_two(list_):
    pass


def all_possible_concatenations_of_two(list_):
    string_combinations = combinations(map(str, list_), 2)
    string_concatenations = chain(*[[s[0] + s[1], s[1] + s[0]] for s in string_combinations])
    return list(map(int, string_concatenations))


def combinations_in_sum_order(list_, r):
    if len(list_) < r:
        return
    if r == 1:
        for element in list_:
            yield [element]
        return
    for combination in combinations_in_sum_order(list_[:-1], r):
        yield combination
    for partial_combination in combinations_in_sum_order(list_[:-1], r - 1):
        yield partial_combination + [list_[-1]]


ELEMENTS = 4


def main():
    primes_ = primes_up_to(1000)[1:]  # skip 2
    primes_to_check_against = primes_up_to(1000000)

    for combination in combinations_in_sum_order(primes_, ELEMENTS):
        for combination_with_one_less_element in combinations(combination, ELEMENTS - 1):
            for possible_prime in all_possible_concatenations_of_two(combination_with_one_less_element):
                if not possible_prime in primes_to_check_against:
                    break

        for possible_prime in all_possible_concatenations_of_two(combination):
            if not possible_prime in primes_to_check_against:
                break
        else:
            print(combination, all_possible_concatenations_of_two(combination))
            break


if __name__ == '__main__':
    main()
