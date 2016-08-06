from functools import lru_cache
from itertools import chain
from itertools import combinations

from primes import primes_up_to


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


@lru_cache(maxsize=None)
def combinations_of_pair_are_primes(pair):
    global all_primes
    strings = list(map(str, pair))
    combinations = [strings[0] + strings[1], strings[1] + strings[0]]
    ints = map(int, combinations)
    for i in ints:
        if not i in all_primes:
            return False
    return True


def pairs_from_list(list_):
    return list(combinations(list_, 2))


def have_only_prime_combinations(list_):
    pairs = pairs_from_list(list_)
    for pair in pairs:
        if not combinations_of_pair_are_primes(pair):
            return False
    return True


all_primes = []
ELEMENTS = 5


def main():
    global all_primes
    primes_ = primes_up_to(1000)
    primes_.remove(2)  # should never work
    primes_.remove(5)  # should never work
    all_primes = primes_up_to(1000000)

    for combination in combinations_in_sum_order(primes_, ELEMENTS):
        print(combination)
        if have_only_prime_combinations(combination):
            print(combination, sum(combination))
            return



            # for combination in combinations_in_sum_order(primes_, ELEMENTS):
            #     for combination_with_one_less_element in combinations(combination, ELEMENTS - 1):
            #         for possible_prime in all_possible_concatenations_of_two(combination_with_one_less_element):
            #             if not possible_prime in primes_to_check_against:
            #                 break
            #
            #     for possible_prime in all_possible_concatenations_of_two(combination):
            #         if not possible_prime in primes_to_check_against:
            #             break
            #     else:
            #         print(combination, all_possible_concatenations_of_two(combination))
            #         break


if __name__ == '__main__':
    main()
