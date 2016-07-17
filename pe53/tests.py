import unittest

from pe53.card import Card
from pe53.hand import Hand


class CardTests(unittest.TestCase):
    def test_get_value(self):
        c = Card('2H')
        self.assertEquals(c.value, Card.Value.two)

    def test_get_suite(self):
        c = Card('2H')
        self.assertEquals(c.suite, 'H')

    def test_compare_ace_and_king(self):
        c1 = Card('KH')
        c2 = Card('AH')
        self.assertGreater(c2.value, c1.value)

    def test_compare_suites(self):
        c1 = Card('KH')
        c2 = Card('AH')
        self.assertEqual(c1.suite, c2.suite)


class HandTests(unittest.TestCase):
    def test_higher_pair_wins(self):
        h1 = Hand('AH AC 3D 4S 5H')
        h2 = Hand('KH KC 3D 4S 5H')
        self.assertGreater(h1, h2)

    def test_low_pair_beats_highest(self):
        h1 = Hand('AH 6C 3D 4S 5H')
        h2 = Hand('KH KC 3D 4S 5H')
        self.assertGreater(h2, h1)
