import unittest

from primes import primes_up_to


class TestSpiralSquare(unittest.TestCase):
    def test_diameter_1(self):
        self.assertEqual(spiral_square(1), [[1]])

    def test_diameter_3(self):
        self.assertEquals(spiral_square(3), [[5, 4, 3], [6, 1, 2], [7, 8, 9]])


class TestRotateNestedList(unittest.TestCase):
    def test_diameter_2(self):
        self.assertEquals(rotate_nested_list([[4, 3], [1, 2]]), [[1, 4], [2, 3]])


def rotate_nested_list(nested_list):
    translation = zip(*nested_list)
    return [list(reversed(list_)) for list_ in translation]


def spiral_square(d):
    square = [[1]]
    while len(square) < d:
        square = add_2_to_diameter_of_spiral_square(square)
    return square


def add_2_to_diameter_of_spiral_square(square):
    next_value = len(square) ** 2 + 1
    for _ in range(4):
        square = rotate_nested_list(square)
        square.append([])
        for _ in square[0]:
            square[-1].append(next_value)
            next_value += 1
    return square


all_primes = set(primes_up_to(1000000))
prime_diagonals = set()
nonprime_diagonals = {1}

square = [[1]]
while True:
    square = add_2_to_diameter_of_spiral_square(square)
    diagonals = [square[0][0], square[0][-1], square[-1][0], square[-1][-1]]
    for diagonal in diagonals:
        if diagonal in all_primes:
            prime_diagonals.add(diagonal)
        else:
            nonprime_diagonals.add(diagonal)
    quotient = len(prime_diagonals) / (len(prime_diagonals) + len(nonprime_diagonals))
    print(len(square), diagonals, quotient)
    if quotient < 0.1:
        break
