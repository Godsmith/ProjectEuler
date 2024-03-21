from functools import cache
from itertools import count


def first_prime_factor(n):
    if n & 1 == 0:
        return 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d = d + 2
    return n


@cache
def is_prime(n):
    if n == 1:
        return False
    return n == first_prime_factor(n)


values = [1, 1, 1, 1]
step_sizes = [2, 4, 6, 8]
all_values = [1]

for i in count():
    values = [values[i] + step_sizes[i] for i in range(4)]
    step_sizes = [step_size + 8 for step_size in step_sizes]
    all_values.extend(values)
    prime_ratio = len([True for value in all_values if is_prime(value)]) / len(
        all_values
    )
    side_length = 1 + 2 * (i + 1)
    if prime_ratio < 0.1:
        print(side_length)
        break

