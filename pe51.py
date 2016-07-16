from primes import primes_up_to
from itertools import combinations, chain


def create_asterisk_strings(s):
    for i in ['0', '1', '2']:
        if i in s:
            yield s.replace(i, '*')


def numbers_from_string_with_asterisks(s: str):
    ZERO_TO_NINE = list(map(str, range(10)))
    for i in ZERO_TO_NINE:
        yield s.replace('*', i)


flatten = lambda x: list(chain.from_iterable(x))

LIMIT = 1000000

PRIMES = list(filter(lambda x: x > 10, primes_up_to(LIMIT)))

PRIME_STRINGS = list(map(str, PRIMES))

is_prime = {str(i): False for i in range(2, LIMIT + 1)}
for p in PRIME_STRINGS:
    is_prime[p] = True

all_combinations = {}
for i in range(1, 8):
    all_combinations[i] = flatten([[c for c in combinations(range(0, i), r)] for r in range(1, i)])

record_count = 0
record_prime = 0
for s in PRIME_STRINGS:
    print(s)
    asterisk_strings = create_asterisk_strings(s)
    possible_primes_lists = [numbers_from_string_with_asterisks(s) for s in asterisk_strings]
    primes_lists = [[p for p in list_ if not p.startswith('0') and is_prime[p]] for list_ in possible_primes_lists]
    lengths = list(map(len, primes_lists))
    if len(lengths) != 0:
        count = max(lengths)
        if count > record_count:
            record_prime = s
            record_count = count
            if record_count == 8:
                print(record_prime, record_count)
                exit()
