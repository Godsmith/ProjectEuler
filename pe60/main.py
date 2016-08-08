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

    for i, combination in enumerate(combinations(primes_, ELEMENTS)):
        if have_only_prime_combinations(combination):
            print(combination, sum(combination))
            return


def print_pairs_concatenating_to_primes():
    if False:
        global all_primes
        all_primes = primes_up_to(1000000)
        pairs = pairs_from_list(primes_up_to(1000))
        pairs_concatenating_to_primes = list(filter(combinations_of_pair_are_primes, pairs))
        print(pairs_concatenating_to_primes)


def main3():
    from pe60.pairs import pairs_concatenating_to_primes as pairs
    # what we need to do is to find five numbers in pairs that are in pairs with each other
    number_counts = {}
    paired_with_from_number = {}
    numbers = primes_up_to(1000)
    numbers.remove(2)
    numbers.remove(5)
    for number in numbers:
        for pair in pairs:
            if number in pair:
                if not number in number_counts:
                    number_counts[number] = 0
                number_counts[number] += 1

                other_number = [x for x in pair if x != number][0]
                if not number in paired_with_from_number:
                    paired_with_from_number[number] = []
                paired_with_from_number[number].append(other_number)

    numbers_sorted_in_pair_count_order = sorted(numbers, key=lambda x: len(paired_with_from_number[x]))
    pair_counts = [len(paired_with_from_number[x]) for x in numbers_sorted_in_pair_count_order]
    print(pair_counts)
    print(numbers_sorted_in_pair_count_order)
    print(paired_with_from_number)
    print(len([value for value in number_counts.values() if value < 5]))


def find_5_interconnected_pairs(current_numbers, numbers, pairs):
    print(current_numbers)
    for new_number in numbers:
        if len(current_numbers) == 0:
            return find_5_interconnected_pairs(current_numbers + [new_number], numbers, pairs)
        else:
            if new_number <= current_numbers[-1]:
                continue
            for number in current_numbers:
                if not tuple(sorted([new_number, number])) in pairs:
                    break
            else:
                if len(current_numbers) == 4:
                    return current_numbers + [new_number]
                return find_5_interconnected_pairs(current_numbers + [new_number], numbers, pairs)



def main2():
    from pe60.pairs import pairs_concatenating_to_primes as pairs
    # what we need to do is to find five numbers in pairs that are in pairs with each other
    numbers = primes_up_to(1000)
    numbers.remove(2)
    numbers.remove(5)
    print(find_5_interconnected_pairs([], numbers, pairs))


if __name__ == '__main__':
    main2()
