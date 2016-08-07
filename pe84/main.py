from random import randint

from pe84.board import Board
from pe84.card import Card
from pe84.deck import Deck
from pe84.player import Player
from pe84.square import Square


def main():
    cc_deck = Deck()
    cc_deck.add_card(Card.create(Card.Type.GOTO_NEXT_OF_TYPE, square_type=Square.Type.GO))
    cc_deck.add_card(Card.create(Card.Type.GOTO_NEXT_OF_TYPE, square_type=Square.Type.JAIL))
    for _ in range(14):
        cc_deck.add_card(Card.create(Card.Type.NOOP))

    ch_deck = Deck()
    ch_deck.add_card(Card.create(Card.Type.GOTO_NEXT_OF_TYPE, square_type=Square.Type.GO))
    ch_deck.add_card(Card.create(Card.Type.GOTO_NEXT_OF_TYPE, square_type=Square.Type.JAIL))
    ch_deck.add_card(Card.create(Card.Type.GOTO_NUMBER_OF_TYPE, square_type=Square.Type.C, square_number=1))
    ch_deck.add_card(Card.create(Card.Type.GOTO_NUMBER_OF_TYPE, square_type=Square.Type.E, square_number=3))
    ch_deck.add_card(Card.create(Card.Type.GOTO_NUMBER_OF_TYPE, square_type=Square.Type.H, square_number=2))
    ch_deck.add_card(Card.create(Card.Type.GOTO_NUMBER_OF_TYPE, square_type=Square.Type.R, square_number=1))
    ch_deck.add_card(Card.create(Card.Type.GOTO_NEXT_OF_TYPE, square_type=Square.Type.R))
    ch_deck.add_card(Card.create(Card.Type.GOTO_NEXT_OF_TYPE, square_type=Square.Type.R))
    ch_deck.add_card(Card.create(Card.Type.GOTO_NEXT_OF_TYPE, square_type=Square.Type.U))
    ch_deck.add_card(Card.create(Card.Type.GO_BACK_THREE_STEPS))
    for _ in range(6):
        ch_deck.add_card(Card.create(Card.Type.NOOP))

    board = Board(community_chest_deck=cc_deck, chance_deck=ch_deck)
    board.add_square(Square.create(Square.Type.GO))
    board.add_square(Square.create(Square.Type.A))
    board.add_square(Square.create(Square.Type.CC))
    board.add_square(Square.create(Square.Type.A))
    board.add_square(Square.create(Square.Type.T))
    board.add_square(Square.create(Square.Type.R))
    board.add_square(Square.create(Square.Type.B))
    board.add_square(Square.create(Square.Type.CH))
    board.add_square(Square.create(Square.Type.B))
    board.add_square(Square.create(Square.Type.B))

    board.add_square(Square.create(Square.Type.JAIL))
    board.add_square(Square.create(Square.Type.C))
    board.add_square(Square.create(Square.Type.U))
    board.add_square(Square.create(Square.Type.C))
    board.add_square(Square.create(Square.Type.C))
    board.add_square(Square.create(Square.Type.R))
    board.add_square(Square.create(Square.Type.D))
    board.add_square(Square.create(Square.Type.CC))
    board.add_square(Square.create(Square.Type.D))
    board.add_square(Square.create(Square.Type.D))

    board.add_square(Square.create(Square.Type.FP))
    board.add_square(Square.create(Square.Type.E))
    board.add_square(Square.create(Square.Type.CH))
    board.add_square(Square.create(Square.Type.E))
    board.add_square(Square.create(Square.Type.E))
    board.add_square(Square.create(Square.Type.R))
    board.add_square(Square.create(Square.Type.F))
    board.add_square(Square.create(Square.Type.F))
    board.add_square(Square.create(Square.Type.U))
    board.add_square(Square.create(Square.Type.F))

    board.add_square(Square.create(Square.Type.G2J))
    board.add_square(Square.create(Square.Type.G))
    board.add_square(Square.create(Square.Type.G))
    board.add_square(Square.create(Square.Type.CC))
    board.add_square(Square.create(Square.Type.G))
    board.add_square(Square.create(Square.Type.R))
    board.add_square(Square.create(Square.Type.CH))
    board.add_square(Square.create(Square.Type.H))
    board.add_square(Square.create(Square.Type.T))
    board.add_square(Square.create(Square.Type.H))

    player = Player(board)

    frequencies = dict()
    ITERATIONS = 1000000
    for i in range(ITERATIONS):
        player.move(randint(1, 4) + randint(1, 4))
        if not player.square_number in frequencies:
            frequencies[player.square_number] = 0
        frequencies[player.square_number] += 1
    numbers_and_probabilities = [(key, value / ITERATIONS) for key, value in frequencies.items()]
    print(sorted(numbers_and_probabilities, key=lambda x: x[1], reverse=True))


if __name__ == '__main__':
    main()
