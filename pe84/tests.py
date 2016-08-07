import unittest

from pe84.board import Board
from pe84.card import Card
from pe84.deck import Deck
from pe84.player import Player
from pe84.square import Square


class SquareTests(unittest.TestCase):
    def test_to_string(self):
        square = Square.create(Square.Type.GO)
        self.assertEquals('GO', str(square))
        square = Square.create(Square.Type.CC)
        self.assertEquals('CC', str(square))
        square = Square.create(Square.Type.CH)
        self.assertEquals('CH', str(square))
        square = Square.create(Square.Type.G2J)
        self.assertEquals('G2J', str(square))
        square = Square.create(Square.Type.JAIL)
        self.assertEquals('JAIL', str(square))


class BoardTests(unittest.TestCase):
    def test_add_square(self):
        board = Board()
        board.add_square(Square.create(Square.Type.GO))
        board.add_square(Square.create(Square.Type.CC))
        self.assertEquals('GO CC', str(board))


class PlayerTests(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board.add_square(Square.create(Square.Type.GO))
        self.board.add_square(Square.create(Square.Type.JAIL))
        self.player = Player(self.board)

    def test_starting_square_type(self):
        self.assertEquals(Square.Type.GO, self.player.square_type)

    def test_starting_square_number(self):
        self.assertEquals('00', self.player.square_number)

    def test_move(self):
        self.player.move(1)
        self.assertEquals(Square.Type.JAIL, self.player.square_type)

    def test_move_twice(self):
        self.board.add_square(Square.create(Square.Type.JAIL))
        self.player.move(1)
        self.player.move(1)
        self.assertEquals(Square.Type.JAIL, self.player.square_type)

    def test_move_rollover(self):
        self.player.move(2)
        self.assertEquals(Square.Type.GO, self.player.square_type)


class TestGoToJail(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board.add_square(Square.create(Square.Type.GO))
        self.board.add_square(Square.create(Square.Type.G2J))
        self.board.add_square(Square.create(Square.Type.JAIL))
        self.player = Player(self.board)

    def test_g2j(self):
        self.player.move(1)
        self.assertEquals(Square.Type.JAIL, self.player.square_type)

    def test_wraparound(self):
        self.board.add_square(Square.create(Square.Type.G2J))
        self.player.move(3)
        self.assertEquals(Square.Type.JAIL, self.player.square_type)


class TestDeck(unittest.TestCase):
    def test_shuffling_one_card_deck(self):
        deck = Deck()
        deck.add_card(Card.create(Card.Type.GOTO))
        deck.shuffle()
        self.assertEquals(Card.Type.GOTO, deck.pop().card_type)

    def test_popping_several_cards(self):
        deck = Deck()
        deck.add_card(Card.create(Card.Type.GOTO))
        deck.add_card(Card.create(Card.Type.NOOP))
        deck.add_card(Card.create(Card.Type.GOTO))
        self.assertEquals(Card.Type.GOTO, deck.pop().card_type)
        self.assertEquals(Card.Type.NOOP, deck.pop().card_type)
        self.assertEquals(Card.Type.GOTO, deck.pop().card_type)
        self.assertEquals(Card.Type.GOTO, deck.pop().card_type)

    def test_going_to_jail_due_to_g2j_card(self):
        cc_deck = Deck()
        cc_deck.add_card(Card.create(Card.Type.GOTO, square_type=Square.Type.JAIL))
        board = Board(community_chest_deck=cc_deck)
        board.add_square(Square.create(Square.Type.GO))
        board.add_square(Square.create(Square.Type.JAIL))
        board.add_square(Square.create(Square.Type.CC))
        player = Player(board)
        player.move(2)
        self.assertEquals(Square.Type.JAIL, player.square_type)

    def test_going_to_go_due_to_g2go_card(self):
        cc_deck = Deck()
        cc_deck.add_card(Card.create(Card.Type.GOTO, square_type=Square.Type.GO))
        board = Board(community_chest_deck=cc_deck)
        board.add_square(Square.create(Square.Type.GO))
        board.add_square(Square.create(Square.Type.JAIL))
        board.add_square(Square.create(Square.Type.CC))
        player = Player(board)
        player.move(1)
        player.move(1)
        self.assertEquals(Square.Type.GO, player.square_type)
