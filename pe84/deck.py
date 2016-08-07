class Deck(object):
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        pass

    def pop(self):
        card = self.cards.pop()
        self.cards.insert(0, card)
        return card
