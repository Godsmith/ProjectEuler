import unittest

from pe58 import spiral_square, add_2_to_diameter_of_spiral_square, rotate_nested_list


class TestSpiralSquare(unittest.TestCase):
    def test_diameter_1(self):
        self.assertEqual(spiral_square(1), [[1]])

    def test_diameter_3(self):
        self.assertEquals(spiral_square(3), [[5, 4, 3], [6, 1, 2], [7, 8, 9]])


class TestAddLayerToSpriralSquare(unittest.TestCase):
    def test_diameter_1(self):
        self.assertEquals(add_2_to_diameter_of_spiral_square([[1]]), [[5, 4, 3], [6, 1, 2], [7, 8, 9]])

    def test_diameter_3(self):
        self.assertEquals(add_2_to_diameter_of_spiral_square([[5, 4, 3], [6, 1, 2], [7, 8, 9]]),
                                                             [[17,16,15,14,13],
                                                              [18, 5, 4, 3,12],
                                                              [19, 6, 1, 2,11],
                                                              [20, 7, 8, 9,10],
                                                              [21,22,23,24,25]])


class TestRotateNestedList(unittest.TestCase):
    def test_diameter_2(self):
        self.assertEquals(rotate_nested_list([[4, 3], [1, 2]]), [[1, 4], [2, 3]])
