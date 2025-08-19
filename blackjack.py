# Cianna Grama 
# Programming Assignment 5
# Intro to Computer Science
# blackjack.py

# Playable blackjack game with graphics GUI

from graphics import *
from PlayingCards import *
from Deck import *
from random import *
from Button import *
from time import sleep

class Blackjack:

    """Attributes of this Blackjack class are as follows.
       INSTANCE VARIABLES

        dealerHand: a list of PlayingCard objects representing the dealer's hand
        playerHand: a list of PlayingCard objects representing the player's hand
        playingDeck: a Deck object representing the deck of cards the game is being played with
        
       METHODS
       
        __init__(self, dHand=[], pHand=[])
            constructor that initializes instance variables
            it also gives the playingDeck an initial shuffle
            
        initDeal(self,gwin,xposD,yposD,xposP,yposP):
            deals out initial cards, 2 per player and 
            displays dealer and player hands on graphical win
            xposD and yposD give initial position for dealer cards
            xposP and yposP are analogous
            
        hit(self, gwin, xPos, yPos)
            adds a new card to the player's hand and places it at xPos, yPos
            
        evaluateHand(self, hand)
            totals the cards in the hand that is passed in and returns total
            (ace counts as 11 if doing so allows total to stay under 21)
            
        dealearPlays(self, gwin, xPos, yPos)
            dealer deals cards to herself, stopping when hitting "soft 17"
    """


    # creates the initial variables and creates 2 empty lists for the dealer hand and player hand
    def __init__(self):

        # create empty hands
        self.dealerHand = []
        self.playerHand = []

        # create a deck for the game with 52 cards
        self.playingDeck = Deck()

        # give the playing deck an initial shuffle
        self.playingDeck.shuffle()


    def dealCard(self, win, Xpos, Ypos):
        
        # deal top card from shuffled deck
        dealtcard = self.playingDeck.dealCard()

        # find the rank and suit
        rank = dealtcard.getRank()
        suit = dealtcard.getSuit()

        # draw the dealt card in the gui
        drawImageCard(win, rank, suit, Xpos, Ypos)

        # print(self.playingDeck.cardsLeft())

        return dealtcard


    # deal 2 cards to player and 2 to the dealer
    def initDeal(self, win):

    # deal 2 cards to the player

        # deal 1 top card in the players hand area
        dealtCard = self.dealCard(win, 30, 10)
    
        # add the 1st card to the player's hand
        self.playerHand.append(dealtCard)
        
        # deal 2nd card into players hand area
        dealtCard = self.dealCard(win, 40, 10)

        # add the 2nd card to the player's hand
        self.playerHand.append(dealtCard)

    # deal 2 cards to the dealer
    
        # deal 1 top card in the dealers hand area
        dealtCard = self.dealCard(win, 40, 90)
    
        # add the 1st card to the dealer's hand
        self.dealerHand.append(dealtCard)

        # draw the image of the back of the card on the screen over the first dealt card
        backCardimage = Image(Point(40, 90), "playingcards/b2fv.gif")
        backCardimage.draw(win)
        
        # deal 2nd card into dealers hand area
        dealtCard = self.dealCard(win, 50, 90)

        # add the 2nd card to the dealer's hand
        self.dealerHand.append(dealtCard)

        return backCardimage


    def evaluateHand(self, hand):
        
        handtotal = 0

        foundAce = False

        softAce = False

        # for each card in the hand
        for card in hand:

            # if the card value is 1
            if card.value() == 1:

                # there is an ace in the hand
                foundAce = True

            # add the card value to the hand value
            handtotal += card.value()

        # if there is an ace and the hand total is less than or equal to 11    
        if foundAce and handtotal <= 11:

            # add 10 to the hand total
            handtotal += 10

            softAce = True

        # return the hand total    
        return handtotal


    def evaluateVisibleDealerHand(self, hand): 
        
        value = self.evaluateHand([self.dealerHand[-1]])
        
        return value


    def dealerPlays(self, win):

        # evaluate the total in the dealer's hand
        handvalue = self.evaluateHand(self.dealerHand)

        # set value for placing cards to 0
        place = 0

        # while the total in the dealer's hand is less than 17, deal a card on screen and into the dealer hand list
        while handvalue < 17:

            # add a card to the dealer's hand (on screen)
            dealtcard = self.dealCard(win, 60 + place, 90)

            # add 10 to the place value in case another card is added to the dealer hand
            place += 10
            
            # add the card to the dealer's hand list 
            self.dealerHand.append(dealtcard)
            handvalue = self.evaluateHand(self.dealerHand)

            # wait 1 second before adding another card value
            sleep(1)

        # return the dealer's hand 
        return self.dealerHand
            
          
##################### HELPER FUNCTIONS #####################
    
def drawImageCard(win, rank, suit, xPos, yPos):

    # create image at given position and call corresponding playing card image
    im = Image(Point(xPos, yPos), "playingcards/" + suit + str(rank) + ".gif")

    im.draw(win)
    
def dealpage(win):

    # create intro page with deal button
    dealButton = Button(win, Point(50, 50), 15, 10, "Deal")

    return dealButton

def bustpage(win, hitbutton, standbutton):

    # deactivate hitbutton and standbutton
    hitbutton.deactivate()
    standbutton.deactivate()

    # run the lose page
    losepage(win)

    # draw bust on screen around white box
    bustText = Text(Point(50, 70), "BUST!")
    bustText.setSize(40)
    bustText.setFill("red")
    
    bustBox = Rectangle(Point(40, 65), Point(60, 75))
    bustBox.setFill("lightgrey")

    bustBox.draw(win)                   
    bustText.draw(win)
    
def losepage(win):

    # set background to gray
    win.setBackground("gray")

    # write you lose on the screen around a white box
    loseText = Text(Point(50, 50), "YOU LOSE")
    loseText.setSize(60)
    loseText.setFill("red")

    loseBox = Rectangle(Point(25, 40), Point(75, 60))
    loseBox.setFill("white")

    loseBox.draw(win)                   
    loseText.draw(win)

def winpage(win):

    # write you win on the screen around a white box
    winText = Text(Point(50, 50), "YOU WIN!")
    winText.setSize(60)
    winText.setFill("green")

    winBox = Rectangle(Point(25, 40), Point(75, 60))
    winBox.setFill("white")

    winBox.draw(win)                   
    winText.draw(win)


def tiepage(win):

    # write tie on the screen around a white box
    winText = Text(Point(50, 50), "PUSH (tie)")
    winText.setSize(60)

    winBox = Rectangle(Point(25, 40), Point(75, 60))
    winBox.setFill("white")

    winBox.draw(win)                   
    winText.draw(win)


##################### MAIN FUNCTION ##################### 

def main():

    # create gui
    win = GraphWin("Blackjack", 800, 800)
    win.setCoords(0, 0, 100, 100)
    win.setBackground("green")

    # start Blackjack class
    game = Blackjack()

    # run deal page with deal button and return deal button
    dealButton = dealpage(win)

    # get a mouse click
    pt = win.getMouse()

    # while the deal button is not clicked
    while not dealButton.isClicked(pt):

        # get a mouse click
        pt = win.getMouse()

# when the deal button is clicked: create the game gui page 
    # undraw everything on the dealpage
    dealButton.undraw()

    # create hit button
    hitButton = Button(win, Point(10, 50), 15, 10, "Hit")

    # create stand button
    standButton = Button(win, Point(90, 50), 15, 10, "Stand")

    # create quit button
    quitButton = Button(win, Point(90, 5), 10, 5, "Quit")

    # use the deal method from the blackjack class and return the back card image
    backCardImage = game.initDeal(win)

    # create a text box that tells the player where the dealer points are 
    dealerText = Text(Point(90, 80), "Dealer")
    dealerText.setSize(20)
    dealerText.setFill("red")
    dealerText.draw(win)

    # evaluate points for dealer of the visible card (only 1)
    dealerpoints = game.evaluateVisibleDealerHand(game.dealerHand)
    
    # create a text box that displays the dealer's points of the visible card (only 1)
    dealerPointsText = Text(Point(90, 75), dealerpoints)
    dealerPointsText.setSize(60)
    dealerPointsText.setFill("red")
    dealerPointsText.draw(win)

    # create a text box that tells the player where the player points are 
    playerText = Text(Point(90, 30), "Player")
    playerText.setSize(20)
    playerText.draw(win)

    # evaluate points for player
    playerpoints = game.evaluateHand(game.playerHand)
    
    # create a text box that displays the player's points
    playerPointsText = Text(Point(90, 25), playerpoints)
    playerPointsText.setSize(60)
    playerPointsText.draw(win)

# get a mouse click
    pt = win.getMouse()

    # set n equal to 0
    n = 0
    
    # while quit button is not pressed
    while not quitButton.isClicked(pt):


        # if hit button is clicked
        if hitButton.isClicked(pt):

            # deal 1 top card in the players hand area
            dealtCard = game.dealCard(win, 50 + n, 10)
            n += 10
            
            # add the hit card to the players's hand
            game.playerHand.append(dealtCard)

            # reevalutate hand and set player points to current points for the player
            playerpoints = game.evaluateHand(game.playerHand)
            playerPointsText.setText(playerpoints)

            # if the playerpoints are greater than 21, run the bust page screen
            if playerpoints > 21:

                sleep(0.5)

                # reveal the hole card by undrawing the back card
                backCardImage.undraw()

                # update the dealer point values to reflect the actual points
                game.dealerpoints = game.evaluateHand(game.dealerHand)
                dealerPointsText.setText(game.dealerpoints)

                # run bust page, which includes you lose page and a message telling the user that they busted
                bustpage(win, hitButton, standButton)
            
        # if stand button is clicked
        if standButton.isClicked(pt):

            # deactivate the hit button and stand button
            hitButton.deactivate()
            standButton.deactivate()

            # reveal the hole card by undrawing the back card
            backCardImage.undraw()

            # update the dealer point values to reflect the actual points
            game.dealerpoints = game.evaluateHand(game.dealerHand)
            dealerPointsText.setText(game.dealerpoints)

            sleep(0.5)

            # deal cards to dealer while the hand is less than 17 and return the dealer's hand list and set that equal to the dealer's hand list for the whole game
            game.dealerhand = game.dealerPlays(win)
            
            # find the dealer's new point value and update it in the gui 
            game.dealerpoints = game.evaluateHand(game.dealerHand)
            dealerPointsText.setText(game.dealerpoints)                        

            # evaluate the playerpoints 
            game.playerpoints = game.evaluateHand(game.playerHand)

            # make simpler variables
            playerpoints = game.playerpoints
            dealerpoints = game.dealerpoints

            # if dealer points are greater than 21, you win
            if dealerpoints > 21:

                winpage(win)
                
            # if dealer poins are not greater than 21
            else:
                if playerpoints > dealerpoints:

                    winpage(win)

                elif playerpoints < dealerpoints:

                    losepage(win)

                elif playerpoints == dealerpoints:

                    tiepage(win)

        # get another mouse click while quit button is not clicked 
        pt = win.getMouse()

    # close the window when the quit button is clicked 
    win.close()

    
if __name__ == "__main__":
    main()


        

        

        

    
