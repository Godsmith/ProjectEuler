# -*- coding: utf-8 -*-
""" The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""
from primes import prime_factors
def main():
    consecutive_count = 0
    for i in range(1000,1000000):
        factors = prime_factors(i)
        if len(set(factors)) == 4:
            consecutive_count += 1
        else:
            consecutive_count = 0
        if consecutive_count == 4:
            for j in range(i-3, i+1):
                print('%s: %s' % (j, factors))
            return




if __name__ == "__main__":
    main()
