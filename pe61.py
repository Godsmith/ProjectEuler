import unittest


class TestPolygonalNumbers(unittest.TestCase):
    def test_triangle(self):
        self.assertEquals(list(map(triangle, range(1, 6))), [1, 3, 6, 10, 15])

    def test_square(self):
        self.assertEquals(list(map(square, range(1, 6))), [1, 4, 9, 16, 25])

    def test_pentagonal(self):
        self.assertEquals(list(map(pentagonal, range(1, 6))), [1, 5, 12, 22, 35])

    def test_hexagonal(self):
        self.assertEquals(list(map(hexagonal, range(1, 6))), [1, 6, 15, 28, 45])

    def test_heptagonal(self):
        self.assertEquals(list(map(heptagonal, range(1, 6))), [1, 7, 18, 34, 55])

    def test_octagonal(self):
        self.assertEquals(list(map(octagonal, range(1, 6))), [1, 8, 21, 40, 65])


def triangle(n):
    return int(n * (n + 1) / 2)


def square(n):
    return int(n ** 2)


def pentagonal(n):
    return int(n * (3 * n - 1) / 2)


def hexagonal(n):
    return int(n * (2 * n - 1))


def heptagonal(n):
    return int(n * (5 * n - 3) / 2)


def octagonal(n):
    return int(n * (3 * n - 2))


def four_digit_values_of(f):
    values = []
    i = 1
    while True:
        value = str(f(i))
        length = len(value)
        if length == 4:
            values.append(value)
        elif length > 4:
            return values
        i += 1


def possible_continuations(s, remaining_functions, four_digit_values_from_function, function_and_values, original):
    if len(remaining_functions) == 0:
        if original.startswith(s[2:]):
            print(list(map(lambda x: x[1], function_and_values)))
            return
    # print('possible continuations, testing %s with %s functions left' % (s, len(remaining_functions)))
    for function in remaining_functions:
        valid_values = [value for value in four_digit_values_from_function[function] if value.startswith(s[2:])]
        for value in valid_values:
            new_remaining_functions = list(remaining_functions)
            new_remaining_functions.remove(function)
            new_function_and_values = list(function_and_values)
            new_function_and_values.append((function, value))
            possible_continuations(value, new_remaining_functions, four_digit_values_from_function, new_function_and_values, original)


def main():
    functions = (triangle, square, pentagonal, hexagonal, heptagonal, octagonal)
    four_digit_values_from_function = {function: four_digit_values_of(function) for function in functions}

    functions_except_octagonal = list(functions)
    functions_except_octagonal.remove(octagonal)

    for value in four_digit_values_from_function[octagonal]:
        possible_continuations(value, functions_except_octagonal, four_digit_values_from_function, [(octagonal, value)], value)


if __name__ == '__main__':
    main()
