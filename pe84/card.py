from enum import Enum


class Card(object):
    class Type(Enum):
        NOOP = 1,
        GOTO = 2

    def __init__(self, card_type, square_type, square_number):
        self.card_type = card_type
        self.square_type = square_type
        self.square_number = square_number

    @staticmethod
    def create(card_type, square_type=None, square_number=None):
        return Card(card_type, square_type, square_number)

    def get_new_position(self, board, position):
        if self.card_type == Card.Type.GOTO:
            return board.get_position_of_next(self.square_type, position)
        else:
            return position
