from enum import IntEnum


class Card():
    class Value(IntEnum):
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5
        six = 6
        seven = 7
        eight = 8
        nine = 9
        ten = 10
        jack = 11
        queen = 12
        king = 13
        ace = 14

        @classmethod
        def from_string(cls, s):
            d = {'T': 10,
                 'J': 11,
                 'Q': 12,
                 'K': 13,
                 'A': 14}
            if s in d:
                return cls(d[s])
            else:
                return cls(int(s))

    def __init__(self, s):
        self._value = Card.Value.from_string(s[0])
        self._suite = s[1]
        self._string = s

    def __repr__(self):
        return self._string

    @property
    def value(self):
        return self._value

    @property
    def suite(self):
        return self._suite
