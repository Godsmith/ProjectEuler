"""The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
from primes import primes_up_to
from math import sqrt

LIMIT = 1000

primes = primes_up_to(LIMIT)

start = 0
end = 0
record_count = 0
record_prime = 0
searched = [[False for i in range(LIMIT)] for j in range(LIMIT)]
while start < int(sqrt(LIMIT)):
    psum = sum(primes[start:end])
    count = end - start + 1
    searched[start][end] = True
    print(psum, primes[start:end])
    if psum > LIMIT and count - 1 > record_count:
        if not searched[start][end-1]:
            end -= 1
        else:
            start += 1
    else:
        if psum in primes:
            record_prime = psum
            record_count = count
        end += 1

print(record_count, record_prime)
