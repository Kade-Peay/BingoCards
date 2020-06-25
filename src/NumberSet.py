import random


class NumberSet:
    def __init__(self, size, maxNum):
        """NumberSet constructor"""
        self.size = size
        self.maxNum = maxNum
        self.numList = []
        self.nxt = -1

        listSize = self.getSize()
        while len(self.numList) < listSize:
            j = random.randrange(1, int(self.maxNum))
            if j not in self.numList:
                self.numList.append(j)

        self.randomize()
        if listSize % 2 != 0:
            midPoint = (len(self.numList) // 2)
            self.numList[midPoint] = "FREE!"


    def getSize(self):
        """Return an integer: the size of the NumberSet"""
        return int(self.size) ** 2

    def get(self, index):
        """Return an integer: get the number from this NumberSet at an index"""
        return self.numList[index]

    def randomize(self):
        """void function: Shuffle this NumberSet"""
        for i in self.numList:
            return random.randrange(1, int(self.maxNum))

    def getNext(self):
        """Return an integer: when called repeatedly return successive values
        from the NumberSet until the end is reached, at which time 'None' is returned"""
        while self.nxt < len(self.numList):
            self.nxt += 1
            if self.nxt > len(self.numList) - 1:
                return 'None'
            else:
                return self.numList[self.nxt]

