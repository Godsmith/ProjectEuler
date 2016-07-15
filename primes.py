from math import sqrt
from functools import lru_cache

@lru_cache(maxsize=None)
def primes_up_to(n):
    is_prime = [True] * n
    for i in range(2,int(sqrt(n))):
        j = 2 * i
        while j < n:
            is_prime[j] = False
            j += i
    return [i for i, x in enumerate(is_prime) if x][2:]


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



