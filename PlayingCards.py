# Ta check planning

from random import *
  
class PlayingCards:

    def __init__(self, rank, suit):

        # user inputs integer 1 - 13 for rank
        # user inputs letter for suit
        
        # rank is integer in range 1-13 ace-king
        # suit is single character d, c, h, s indicating suit
        # this function creates a correspnding card

        self.rank = rank

        self.suit = suit 

    def getRank(self):

        # return rank of card
        return self.rank

    def getSuit(self):

        # return suit of card
        return self.suit

    def value(self):

        # returns blackjack value of the card
        # (ace = 1, face cards count as 10)
        if 1 <= self.rank <= 9:
            
            return self.rank
        
        elif self.rank >= 10:
            
            return 10


    def __str__(self):

        ranks = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
        suits = {"s" : "Spades", "c" : "Clubs", "h" : "Hearts", "d" : "Diamonds"}

        rankType = ranks[self.rank - 1]

        suitType = suits[self.suit]

        string = str(rankType) + " of " + suitType
        
        return string


# test card class with a program that prints out n randomly generated cards and the associated blackjack value where n is a number supplied by the user

def main():

    print("Practice")
    
    n = int(input("How many cards would you like to print: "))

    for repeat in range(n):

        rank = randrange(1, 14)

        suit = "s"

        card = PlayingCards(rank, suit)

        print("\n", card, "\t", card.value())

if __name__ == "__main__":
    
    main()




