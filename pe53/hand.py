from enum import IntEnum
from typing import List

from pe53.card import Card


class Hand:
    class Combination(IntEnum):
        highest = 1
        pair = 2

    def __init__(self, s):
        card_strings = s.split()
        self._cards = [Card(s) for s in card_strings]

    def __gt__(self, other):
        return (self.combination >= other.combination and
                self.value > other.value)

    @property
    def _combination_and_combination_value(self) -> (Combination, List[Card]):
        value_count = {}
        for card in self._cards:
            value_count[card.value] = value_count.get(card.value, 0) + 1
        if max(value_count.values()) == 2:
            for value in value_count:
                if value_count[value] == 2:
                    return_value = value
            return (Hand.Combination.pair, return_value)
        else:
            return (Hand.Combination.highest, max([card.value for card in self._cards]))

    @property
    def combination(self):
        return self._combination_and_combination_value[0]

    @property
    def value(self):
        return self._combination_and_combination_value[1]
