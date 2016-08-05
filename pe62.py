import unittest


class TestGetCubesWithDigits(unittest.TestCase):
    def test_1(self):
        self.assertEquals(['1', '8'], get_cubes_with_digits(1))


class TestCountPermutations(unittest.TestCase):
    def test_simple(self):
        self.assertEquals(2, count_permutations('hello',
                                                ['helo', 'helllo', 'olleh', 'loleh']))

    def test_again(self):
        self.assertEquals(1, count_permutations('112233', ['112233',
                                                           '123',
                                                           '1122333',
                                                           '111111',
                                                           '3322111']))


def get_cubes_with_digits(d):
    cubes = []
    i = 1
    while True:
        cube = str(i ** 3)
        length = len(cube)
        if length == d:
            cubes.append(cube)
        elif length > d:
            return cubes
        i += 1


def count_permutations(s, list_):
    sorted_s = sorted(s)
    return len([s1 for s1 in map(sorted, list_) if sorted_s == s1])


def main():
    cubes = get_cubes_with_digits(12)
    for cube in cubes:
        permutations = count_permutations(cube, cubes)
        if permutations == 5:
            print(cube)
            return


if __name__ == '__main__':
    main()
