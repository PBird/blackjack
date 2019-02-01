"""[summary]

Returns:
    [type] -- [description]
"""

import random
from card import Card


class Deck:
    """[summary]

    Returns:
        [type] -- [description]
    """

    def __init__(self, cards=None):
        if not cards:
            cards = []
        if not bool(len(cards)):
            self.deck = [Card(no, shape)
                         for shape in range(0, 4) for no in range(0, 13)]
        else:
            self.deck = cards

    def draw(self):
        """[summary]

        Returns:
            [type] -- [description]
        """

        return self.deck.pop()

    def shuffle(self):
        """[summary]

        Returns:
            [type] -- [description]
        """

        temp_deck = []
        while self.deck:
            temp_deck.append(self.deck.pop(
                random.randint(0, len(self.deck)-1)))
        self.deck = temp_deck
        return self

    def recreate(self, parameter_list):
        """[summary]

        Arguments:
            parameter_list {[type]} -- [description]
        """

    def get(self):
        """[summary]

        Returns:
            [type] -- [description]
        """

        return self.deck

    def __str__(self):
        return '    '.join([card.__str__() for card in self.deck])

    def __len__(self):
        return len(self.deck)

    def add_card(self, card):
        """[summary]

        Arguments:
            card {[type]} -- [description]

        Returns:
            [type] -- [description]
        """

        return self.deck.append(card)


def try_deck():
    """ try to working
    """

    deck = Deck([Card(0, 1), Card(0, 2)])
    deck.shuffle()
    print(len(deck))

if __name__ == '__main__':
    try_deck()
