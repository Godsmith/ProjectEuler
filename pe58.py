import unittest


class TestSpiralSquare(unittest.TestCase):
    def test_diameter_1(self):
        self.assertEqual(spiral_square(1), [[1]])

    def test_diameter_2(self):
        self.assertEquals(spiral_square(2), [[2, 1], [3, 4]])


class TestRotateNestedList(unittest.TestCase):
    def test_diameter_2(self):
        self.assertEquals(rotate_nested_list([[4, 3], [1, 2]]), [[1, 4], [2, 3]])


def rotate_nested_list(nested_list):
    translation = zip(*nested_list)
    return [list(reversed(list_)) for list_ in translation]


def spiral_square(d):
    square = [[1]]
    while len(square) < d:
        square = add_1_to_diameter_of_spiral_square(square)
    return square


def add_1_to_diameter_of_spiral_square(square):
    next_value = len(square) ** 2 + 1
    for _ in range(2):
        square = rotate_nested_list(square)
        square.append([])
        for _ in square[0]:
            square[-1].append(next_value)
            next_value += 1
    return square



primes = set()
nonprimes = set()

# d = None
# while len(primes) / (len(primes) + len(nonprimes)) > 0.1:
#     #d = spiral_square(d, square)
#     pass
