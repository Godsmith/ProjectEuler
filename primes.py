from math import sqrt
from functools import lru_cache


def _sieve_primes(possible, certain=None):
    if possible == []:
        return certain
    if certain == None:
        certain = []
    new_prime = possible[0]
    certain += [new_prime]
    possible = list(filter(lambda x: x % new_prime != 0, possible))
    return sieve_primes(possible, certain)


@lru_cache(maxsize=None)
def primes_up_to(i):
    return _sieve_primes(range(2, i))

@lru_cache(maxsize=None)
def is_prime(i):
    for p in range(2, int(sqrt(i))):
        if i % p == 0:
            return False
    return True


def prime_factors(i: int, factors: list=None):
    if factors is None:
        factors = []
    if is_prime(i):
        return factors + [i]
    for p in range(2, int(sqrt(i))):
        if i % p == 0:
            return prime_factors(i/p, factors + [p])



