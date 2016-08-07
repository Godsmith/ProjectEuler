class Player(object):
    def __init__(self, board):
        self.board = board
        self._position = 0

    @property
    def square_type(self):
        return self.board.squares[self.position].type

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value % len(self.board.squares)

    @property
    def square_number(self):
        position = str(self.position)
        if len(position) == 1:
            position = '0' + position
        return position

    def move(self, steps):
        self.position += steps
        new_position = self.board.change_player_position(self.position)
        self.position = new_position
