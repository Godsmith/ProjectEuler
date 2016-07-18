from enum import IntEnum

from pe53.card import Card


class Hand:
    class Combination(IntEnum):
        highest = 1
        pair = 2
        two_pairs = 3
        three_of_a_kind = 4
        straight = 5
        flush = 6
        full_house = 7
        four_of_a_kind = 8

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
    def _generate_combination_and_combination_value(cards) -> (Combination, Card.Value):
        values = [card.value for card in cards]

        # Flush
        if not (False in [card.suite == cards[0].suite for card in cards]):
            return Hand.Combination.flush, max(values)

        # Straight
        needed_values = [Card.Value(min(values) + i) for i in range(1, 5)]
        if not (False in [value in values for value in needed_values]):
            return Hand.Combination.straight, max(values)

        value_count = {}
        for card in cards:
            value_count[card.value] = value_count.get(card.value, 0) + 1
        sorted_value_counts = sorted(value_count.values())
        if sorted_value_counts == [2, 3]:
            return Hand.Combination.full_house, max(values)
        elif sorted_value_counts == [1, 2, 2]:
            value_of_highest_pair = max(filter(lambda x: value_count[x] == 2, value_count.keys()))
            return Hand.Combination.two_pairs, value_of_highest_pair

        # Pair, three of a kind, four of a kind
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
