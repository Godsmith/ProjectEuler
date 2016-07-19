from fractions import Fraction

from integer_functions import digit_list


def square_root_of_two(a):
    return Fraction(1) + Fraction(1) / (1 + a)


a = Fraction(1)
numerator_has_more_digits = 0
for i in range(1000):
    a = square_root_of_two(a)
    if len(digit_list(a.numerator)) > len(digit_list(a.denominator)):
        numerator_has_more_digits += 1

print(numerator_has_more_digits)
