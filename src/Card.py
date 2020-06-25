import sys

import NumberSet

class Card():
    def __init__(self, idnum, size, numberMax):
        """Card constructor"""
        self.idnum = idnum
        self.size = size
        self.numberMax = numberMax


    def getId(self):
        """Return an integer: the ID number of the card"""
        return self.idnum

    def getSize(self):
        """Return an integer: the size of one dimension of the card.
        A 3x3 card will return 3, a 5x5 card will return 5, etc.
        """
        return self.size

    def print(self, file=sys.stdout):
        """void function:
        Prints a card to the screen or to an open file object"""
        card = NumberSet.NumberSet(self.size, self.numberMax)
        line = '+-----'
        i = 0
        print("ID: " + str(self.idnum + 1), end ='', file=file)
        print(file=file)
        while i < card.getSize():
            if i % int(self.size) == 0:
                if i != 0:
                    print('|', end='', file=file)
                print(file=file)
                print(line * int(self.size) + '+',file=file)
                ind = card.get(i)
                print('|{0:^{1}}'.format(ind, 5), end='', file=file)
                i += 1
            else:
                ind = card.get(i)
                print('|{0:^{1}}'.format(ind, 5), end='', file=file)
                i += 1
        print('|', end='', file=file)
        print(file=file)
        print(line * int(self.size) + '+', file=file)

        # card.printCard(self.numberSet)
