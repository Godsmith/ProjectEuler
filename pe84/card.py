from enum import Enum

from pe84.board import Board


class Card(object):
    class Type(Enum):
        NOOP = 1,
        GOTO_NUMBER_OF_TYPE = 2
        GOTO_NEXT_OF_TYPE = 3
        GO_BACK_THREE_STEPS = 4

    def __init__(self, card_type, square_type, square_number):
        self.card_type = card_type
        self.square_type = square_type
        self.square_number = square_number

    @staticmethod
    def create(card_type, square_type=None, square_number=None):
        return Card(card_type, square_type, square_number)

    def get_new_position(self, board: Board, position):
        if self.card_type == Card.Type.GOTO_NEXT_OF_TYPE:
            return board.get_position_of_next(self.square_type, position)
        elif self.card_type == Card.Type.GOTO_NUMBER_OF_TYPE:
            return board.get_position_of(self.square_type, self.square_number)
        elif self.card_type == Card.Type.GO_BACK_THREE_STEPS:
            return position - 3
        else:
            return position
