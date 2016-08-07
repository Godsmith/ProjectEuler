from pe84.square import Square


class Board():
    def __init__(self, community_chest_deck=None, chance_deck=None):
        self.squares = []
        self.community_chest_deck = community_chest_deck
        self.chance_deck = chance_deck

    def __str__(self, *args, **kwargs):
        return ' '.join(map(str, self.squares))

    def add_square(self, square: Square):
        self.squares.append(square)

    def change_player_position(self, position):
        return self.squares[position].get_new_position(self, position)

    def get_position_of_next(self, type: Square.Type, position: int):
        positions_and_types = [(i, square.type) for i, square in enumerate(self.squares)]
        positions = [x[0] for x in positions_and_types if x[1] == type]
        distances = [(x - position) % len(self.squares) for x in positions]
        return position + min(distances)
