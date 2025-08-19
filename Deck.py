# deck class

from PlayingCards import *
import random


# class represents a deck of cards
class Deck:

    def __init__(self):

        # create empty list for all the cards
        self.cardList = []

        for suit in ["d", "c", "h", "s"]:

            for rank in range(1, 14):
                card = PlayingCards(rank, suit)

                self.cardList.append(card)
                
    def shuffle(self):

        # randomizes the order of the cards

        random.shuffle(self.cardList)

    def dealCard(self):

        # returns a single card from the top deck and removes the card from
        # the deck list
        self.topCard = self.cardList[0]

        self.cardList.remove(self.topCard)

        return self.topCard

    def cardsLeft(self):

        # returns the number of cards remaining in the deck
        return len(self.cardList)


# test program by having it deal out a sequence of n cards from a shuffled
# deck where n is user input
# test program by use deck object to impliment blackjack simulation where pool
# of cards is finite 

def main():
    deck = Deck()
    deck.shuffle()
    topcard = deck.dealCard()
    print(topcard)
    print(deck.cardsLeft())

    
    

if __name__ == "__main__":

    main()
    
