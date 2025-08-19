# Button Class
from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """

        # sets w equal to the width/2 and sets h equal to the height/2
        w,h = width/2.0, height/2.0

        # sets x equal to the x value of the given center point, sets y equal to the y value of the given center point
        x,y = center.getX(), center.getY()
        
        # sets self.xmax equal to the x value of the center plus the width/2, and sets self.xmin equal to the x-value of the center minus the width/2
        self.xmax, self.xmin = x+w, x-w

        # sets self.ymax equal to the y value of the center plus the height/2, and sets self.ymin equal to the y-value of the center minus the height/2
        self.ymax, self.ymin = y+h, y-h

        # sets p1 equal to a point at the points of the minimum x value and the minimum y value (aka the bottom left corner of the button)
        p1 = Point(self.xmin, self.ymin)

        # sets p2 equal to a point at the points of the maximum x value and the maximum y value (aka the top right corner of the button)
        p2 = Point(self.xmax, self.ymax)

        # sets <name of the button>.rect equal to a rectangle created with the given center, height, and width
        self.rect = Rectangle(p1,p2)

        # sets the color of the rectangle of the <name of the button> to light gray
        self.rect.setFill('lightgray')

        # draws the <name of the button> rectangle in the GUI window
        self.rect.draw(win)

        # creates the label of <name of the button> based on the given center and label, sets that equal to <name of the button>.label
        self.label = Text(center, label)

        # draws the <name of the button> label in the GUI
        self.label.draw(win)

        # calls to another method in the class
        self.activate() # Start off all buttons as active. This is how to call another method in this class

    def getLabel(self):
        """Returns the label string of this button."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black') # color the text "black"
        self.rect.setWidth(2)       # set the outline to look bolder
        self.active = True          # set the boolean instance variable that tracks "active"-ness to True

    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill("darkgray") ## color the text "darkgray"
        self.rect.setWidth(1) ## set the outline to look finer/thinner
        self.active = False ## set the boolean instance variable that tracks "active"-ness to False

    def isClicked(self, pt):
        """Returns true if button is active and Point pt is inside"""
        if self.active == True and (self.xmin <= pt.getX() <= self.xmax and self.ymin <= pt.getY() <= self.ymax):
            return True
        else:
            return False

    def undraw(self):
        self.rect.undraw()
        self.label.undraw()
