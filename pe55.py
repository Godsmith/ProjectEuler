from functools import lru_cache

from integer_functions import digit_list


@lru_cache(maxsize=None)
def reverse_integer(i: int) -> int:
    return sum([d * 10 ** i for i, d in enumerate(reversed(digit_list(i)))])


@lru_cache(maxsize=None)
def is_palindrome(i: int) -> bool:
    digits = digit_list(i)
    while len(digits) > 1:
        if digits[0] == digits[-1]:
            digits = digits[1:-1]
        else:
            return False
    return True


lychrel_numbers = 0
for number in range(10000):
    for i in range(50):
        number = number + reverse_integer(number)
        if is_palindrome(number):
            break
    else:
        lychrel_numbers += 1

print(lychrel_numbers)
