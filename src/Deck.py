import sys
import Card
import NumberSet

class Deck():
    def __init__(self, cardSize, cardCount, numberMax):
        """Deck constructor"""
        self.__m_cards = cardSize
        self.__m_cardCount = cardCount
        self.numberMax = numberMax
        self.deck = []

        for i in range(int(self.getCardCount())):
            self.deck.append(Card.Card(i + 1, self.__m_cards, self.numberMax))

            
    def getCardCount(self):
        """Return an integer: the number of cards in this deck"""
        return self.__m_cardCount


    def getCard(self, n):
        """Return card N from the deck"""
        card = None
        n -= 1
        if 0 <= n < int(self.getCardCount()):
            card = Card.Card(n, self.__m_cards, self.numberMax)
        return card


    def print(self, file=sys.stdout, idx=None):
        """void function: Print cards from the Deck
        If an index is given, print only that card.
        Otherwise, print each card in the Deck
        """
        if idx is None:
            for idx in range(1, int(self.__m_cardCount) + 1):
                c = self.getCard(idx)
                c.print(file)
            print('', file=file)
        else:
            self.getCard(idx).print(file)
