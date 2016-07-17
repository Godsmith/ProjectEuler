from enum import IntEnum
from typing import List

from pe53.card import Card


class Hand:
    class Combination(IntEnum):
        highest = 1
        pair = 2
        three_of_a_kind = 3
        straight = 4
        flush = 5
        four_of_a_kind = 6

    def __init__(self, s):
        card_strings = s.split()
        self._cards = [Card(s) for s in card_strings]
        self._combination, self._value = self._generate_combination_and_combination_value(self._cards)

    def __gt__(self, other):
        if self.combination > other.combination:
            return True
        elif self.combination < other.combination:
            return False
        else:
            return self.value > other.value

    def __repr__(self):
        return "<Hand: %s | %s %s>" % (', '.join(map(str, self._cards)), self.combination, self.value)

    @staticmethod
    def _generate_combination_and_combination_value(cards) -> (Combination, List[Card]):
        value_count = {}
        for card in cards:
            value_count[card.value] = value_count.get(card.value, 0) + 1
        for combination, count in [(Hand.Combination.four_of_a_kind, 4),
                                   (Hand.Combination.three_of_a_kind, 3),
                                   (Hand.Combination.pair, 2)]:
            if max(value_count.values()) == count:
                for value in value_count:
                    if value_count[value] == count:
                        return_value = value
                return (combination, return_value)
        else:
            return (Hand.Combination.highest, max([card.value for card in cards]))

    @property
    def combination(self):
        return self._combination

    @property
    def value(self):
        return self._value
