"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""
from primes import primes_up_to


def has_same_digits(x, y):
    xs = str(x)
    ys = str(y)
    for s in xs:
        if s in ys:
            ys = ys.replace(s, "", 1)
    return len(ys) == 0


primes = list(filter(lambda x: x > 999, primes_up_to(9999)))

primes_and_remainders = [(x, primes[i + 1:]) for i, x in enumerate(primes)]

primes_and_remainders_with_same_digits = [(x, list(filter(lambda y: has_same_digits(x, y), remainder))) for x, remainder in
                                          primes_and_remainders]

print(primes_and_remainders_with_same_digits)

for x, remainder in primes_and_remainders_with_same_digits:
    for r in remainder:
        if r + r - x in remainder:
            print(x, r, r + r - x)
