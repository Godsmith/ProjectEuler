from functools import lru_cache
from typing import List


@lru_cache(maxsize=None)
def reverse_integer(i: int) -> int:
    return sum([d * 10 ** i for i, d in enumerate(reversed(_get_digits(i)))])


@lru_cache(maxsize=None)
def is_palindrome(i: int) -> bool:
    digits = _get_digits(i)
    while len(digits) > 1:
        if digits[0] == digits[-1]:
            digits = digits[1:-1]
        else:
            return False
    return True


def _get_digits(i: int) -> List[int]:
    digits = []
    while True:
        digits.append(i % 10)
        i //= 10
        if i // 10 == 0:
            digits.append(i)
            break
    return digits


lychrel_numbers = 0
for number in range(10000):
    for i in range(50):
        number = number + reverse_integer(number)
        if is_palindrome(number):
            break
    else:
        lychrel_numbers += 1

print(lychrel_numbers)
