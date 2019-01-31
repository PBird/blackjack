import random
import Card

class Deck:
    def __init__(self, cards = []):
        if not bool(len(cards)):
            self.deck = [Card.Card(no,shape) for shape in range(0,4) for no in range(0,13)]
        else:
            self.deck = cards
    def draw(self):
        return self.deck.pop()
    def shuffle(self):
        tempDeck = []
        while len(self.deck):
            tempDeck.append(self.deck.pop(random.randint(0,len(self.deck)-1)))
        self.deck = tempDeck
        return self
    def recreate(self, parameter_list):
        pass
    def get(self):
        return self.deck
    def __str__(self):
        return '    '.join([card.__str__() for card in self.deck])
    def __len__(self):
        return len(self.deck)
    def addCard(self,card):
        return self.deck.append(card)

if __name__ == '__main__':
    deck = Deck([Card.Card(0,1), Card.Card(0,2)])
    deck.shuffle()
    print(len(deck))