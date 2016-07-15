"""The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
from primes import primes_up_to
from math import sqrt

LIMIT = 1000000

primes = primes_up_to(LIMIT)

start = 0
count = 1
record_count = 0
record_prime = 0
while start < int(sqrt(LIMIT)):
    end = start + count - 1
    psum = sum(primes[start:end])
    print(psum, primes[start:end])
    if psum > LIMIT:
        start += 1
        count = record_count
    else:
        if psum in primes:
            record_prime = psum
            record_count = count
        count += 1

print(record_count, record_prime)
