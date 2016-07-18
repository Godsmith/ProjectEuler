from enum import IntEnum
from typing import List

from pe53.card import Card


class Hand:
    class Rank(IntEnum):
        highest = 1
        pair = 2
        two_pairs = 3
        three_of_a_kind = 4
        straight = 5
        flush = 6
        full_house = 7
        four_of_a_kind = 8
        straight_flush = 9
        royal_flush = 10

    def __init__(self, s):
        card_strings = s.split()
        self._cards = [Card(s) for s in card_strings]
        self._rank, self._values = self._generate_nonflush_rank_and_values(self._cards)
        flush = not (False in [card.suite == self._cards[0].suite for card in self._cards])
        if flush:
            if self._rank == Hand.Rank.straight:
                if max(self._values) == Card.Value.ace:
                    self._rank = Hand.Rank.royal_flush
                else:
                    self._rank = Hand.Rank.straight_flush
            else:
                self._rank = max(Hand.Rank.flush, self._rank)
                self._values = self._values.sort(reverse=True)



    def __gt__(self, other):
        if self.rank > other.rank:
            return True
        elif self.rank < other.rank:
            return False
        else:
            return self.values > other.values

    def __repr__(self):
        return "<Hand: %s | %s %s>" % (', '.join(map(str, self._cards)), self.rank, self.value)

    @staticmethod
    def _generate_nonflush_rank_and_values(cards) -> (Rank, List[Card.Value]):
        values = [card.value for card in cards]


        # Straight
        needed_values = [Card.Value(min(values) + i) for i in range(1, 5)]
        if not (False in [value in values for value in needed_values]):
            return Hand.Rank.straight, sorted(values, reverse=True)

        # Full house, two pairs
        value_count = {}
        for card in cards:
            value_count[card.value] = value_count.get(card.value, 0) + 1
        sorted_value_counts = sorted(value_count.values())
        if sorted_value_counts == [1, 2, 2]:
            values_in_rank = list(filter(lambda x: value_count[x] == 2, value_count.keys()))
            values_outside_rank = [value for value in values if not value in values_in_rank]
            return Hand.Rank.two_pairs, sorted(values_in_rank, reverse=True) + values_outside_rank
        if sorted_value_counts == [2, 3]:
            return Hand.Rank.full_house, sorted(values, reverse=True)

        # Pair, three of a kind, four of a kind
        for rank, count in [(Hand.Rank.four_of_a_kind, 4),
                            (Hand.Rank.three_of_a_kind, 3),
                            (Hand.Rank.pair, 2)]:
            if max(value_count.values()) == count:
                values_in_rank = list(filter(lambda x: value_count[x] == count, value_count.keys()))
                values_outside_rank = [value for value in values if not value in values_in_rank]
                return rank, sorted(values_in_rank, reverse=True) + values_outside_rank
        else:
            return Hand.Rank.highest, sorted(values, reverse=True)

    @property
    def rank(self):
        return self._rank

    @property
    def values(self):
        return self._values
