from typing import List


def digit_list(i: int) -> List[int]:
    digits = []
    while True:
        digits.append(i % 10)
        i //= 10
        if i // 10 == 0:
            digits.append(i)
            break
    return digits
