from Deck import Deck
from Card import Card

class BlackJack:
    CARDVALUES = ( 1,2,3,4,5,6,7,8,9,10,10,10,10 )
    def __init__(self):
        self.deck = Deck().shuffle()
        self.dealerHand = Deck([self.deck.draw(), self.deck.draw()])
        self.userHand = Deck([self.deck.draw(), self.deck.draw()])
        self.dealerHandValue = self.valueOfDeck(self.dealerHand)
        self.userHandValue = self.valueOfDeck(self.userHand)
        self.isFinish = False
    def valueOfDeck(self,deck):
        cards = [card.number for card in deck.get() ]
        if 0 not in cards:
            return sum([self.CARDVALUES[value] for value in cards])
        else:
            if sum([self.CARDVALUES[value] for value in cards])+10 > 21:
                return sum([self.CARDVALUES[value] for value in cards])
            else:
                return sum([self.CARDVALUES[value] for value in cards])+10

    def stand(self):
        while self.userHandValue > self.dealerHandValue:
                self.dealerHand.addCard(self.deck.draw())
                self.dealerHandValue = self.valueOfDeck(self.dealerHand)
                if self.dealerHandValue > 21:
                    break
        else: 
            print("*******************************")
            self.printHands()
            print(" Dealer WON, You LOST :( ")
            self.isFinish = True
            self.winner = 'dealer'
        print("*******************************")
        self.printHands()
        print(" User WON, Congratulations ..!")
        self.winner = 'user'
        self.isFinish = True
    def hit(self):
        self.userHand.addCard(self.deck.draw())
        self.userHandValue = self.valueOfDeck(self.userHand)
        if self.userHandValue == 21:
            self.stand()
        elif self.userHandValue < 21:
            self.isFinish = False
            print("*******************************")
            self.printHands()
        else:
            print("*******************************")
            self.printHands()
            print(" Dealer WON, You LOST :( ")
            self.isFinish = True
            self.winner = 'dealer'
    def start(self):
        self.printHands()
        while not self.isFinish:
            action = input('Stand or Hit[stand|hit] : ')
            if action == 'stand':
                self.stand()
            elif action == 'hit':
                self.hit()
            else:
                print('Wrong action you should write stand or hit')
                continue
        

    def printHands(self):
        print( 'DEALER Hand : %s    value %d'%(self.dealerHand, self.valueOfDeck(self.dealerHand)))
        print('USER Hand : %s   value %d'%(self.userHand, self.valueOfDeck(self.userHand)))
    
if __name__ == '__main__':
    game = BlackJack()
    game.start()
    