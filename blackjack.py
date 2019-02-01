"""[summary]

Returns:
    [type] -- [description]
"""

from deck import Deck


class BlackJack:
    """[summary]

    Returns:
        [type] -- [description]
    """

    CARDVALUES = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)

    def __init__(self):
        self.deck = Deck().shuffle()
        self.dealer_hand = Deck([self.deck.draw(), self.deck.draw()])
        self.user_hand = Deck([self.deck.draw(), self.deck.draw()])
        self.dealer_hand_value = self.value_of_deck(self.dealer_hand)
        self.user_hand_value = self.value_of_deck(self.user_hand)
        self.is_finish = False
        self.winner = None

    def value_of_deck(self, deck):
        """[summary]

        Arguments:
            deck {[type]} -- [description]

        Returns:
            [type] -- [description]
        """

        cards = [card.number for card in deck.get()]
        if 0 not in cards:
            return sum([self.CARDVALUES[value] for value in cards])
        if sum([self.CARDVALUES[value] for value in cards])+10 > 21:
            return sum([self.CARDVALUES[value] for value in cards])
        return sum([self.CARDVALUES[value] for value in cards])+10

    def stand(self):
        """[summary]
        """

        while self.user_hand_value > self.dealer_hand_value:
            self.dealer_hand.add_card(self.deck.draw())
            self.dealer_hand_value = self.value_of_deck(self.dealer_hand)
            if self.dealer_hand_value > 21:
                break
        else:
            print("*******************************")
            self.print_hands()
            self.is_finish = True
            if self.user_hand_value == self.dealer_hand_value:
                print(" Draw, :O ")
                self.winner = 'draw'
            else:
                self.winner = 'dealer'
                print(" Dealer WON, You LOST :( ")
            return
        print("*******************************")
        self.print_hands()
        print(" User WON, Congratulations ..!")
        self.winner = 'user'
        self.is_finish = True

    def hit(self):
        """[summary]
        """

        self.user_hand.add_card(self.deck.draw())
        self.user_hand_value = self.value_of_deck(self.user_hand)
        if self.user_hand_value == 21:
            self.stand()
        elif self.user_hand_value < 21:
            self.is_finish = False
            print("*******************************")
            self.print_hands()
        else:
            print("*******************************")
            self.print_hands()
            print(" Dealer WON, You LOST :( ")
            self.is_finish = True
            self.winner = 'dealer'

    def start(self):
        """[summary]
        """

        self.print_hands()
        while not self.is_finish:
            action = input('Stand or Hit[stand|hit] : ')
            if action == 'stand':
                self.stand()
            elif action == 'hit':
                self.hit()
            else:
                print('Wrong action you should write stand or hit')
                continue

    def print_hands(self):
        """[summary]
        """

        print('DEALER Hand : %s    value %d' %
              (self.dealer_hand, self.value_of_deck(self.dealer_hand)))
        print('USER Hand : %s   value %d' %
              (self.user_hand, self.value_of_deck(self.user_hand)))


if __name__ == '__main__':
    BlackJack().start()
