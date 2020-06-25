import Deck
import Menu

class UserInterface():
    def __init__(self):
        pass


    def run(self):
        """Present the main menu to the user and repeatedly prompt for a valid command"""
        print("Welcome to the Bingo! Deck Generator\n")
        menu = Menu.Menu("Main")
        menu.addOption("C", "Create a new deck")
        
        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "C":
                self.__createDeck()
            elif command == "X":
                keepGoing = False


    def __createDeck(self):
        """Command to create a new Deck"""
        # Get the user to specify the card size, max number, and number of cards
        menu = Menu.Menu("Create Deck")

        keepGoing = True
        while keepGoing:
            cardSize = input("Enter Card size\n")
            if cardSize.isdigit() and 3 <= int(cardSize) <= 15:
                minMax = 2 * (int(cardSize) ** 2)
                maxMax = 4 * (int(cardSize) ** 2)
                maxNum = input("Enter Max Number between " + str(minMax) + " and " + str(maxMax) +'\n')
                if maxNum.isdigit() and int(maxNum) >= int(minMax) and int(maxNum) <= int(maxMax):
                    numOfCards = input("Enter number of cards\n")
                    if numOfCards.isdigit():
                        # Create a new deck
                        self.__m_currentDeck = Deck.Deck(cardSize, numOfCards, maxNum)
                        keepGoing = False
                    else:
                        print("Please enter number of cards between 1 and 10000")
                        self.run()
                else:
                    print("Please enter max between 2*N*N and 4*N*N")
                    self.run()
            else:
                print("Please enter card between 3 and 15")
                self.run()

        # Display a deck menu and allow use to do things with the deck
        self.__deckMenu()


    def __deckMenu(self):
        """Present the deck menu to user until a valid selection is chosen"""
        menu = Menu.Menu("Deck")
        menu.addOption("P", "Print a card to the screen")
        menu.addOption("D", "Display the whole deck to the screen")
        menu.addOption("S", "Save the whole deck to a file")

        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "P":
                self.__printCard()
            elif command == "D":
                print()
                self.__m_currentDeck.print()
            elif command == "S":
                self.__saveDeck()
            elif command == "X":
                keepGoing = False


    def __printCard(self):
        """Command to print a single card"""
        cardToPrint = self.__getNumberInput()
        if cardToPrint > 0:
            print()
            self.__m_currentDeck.print(idx=cardToPrint)


    def __saveDeck(self):
        """Command to save a deck to a file"""
        fileName = self.__getStringInput()
        if fileName != "":
            # TODO: open a file and pass to currentDeck.print()
            outputStream = open(fileName, 'w')
            self.__m_currentDeck.print(outputStream)
            outputStream.close()
            print("Done!")

    def __getNumberInput(self):
        cardToPrint = input("Enter card ID: \n")
        return int(cardToPrint)

    def __getStringInput(self):
        stringInput = input("Enter output file name: \n")
        return stringInput
