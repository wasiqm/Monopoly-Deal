# button.py
from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

    def setFill(self, colour):
        "Sets the fill of the button to any colour."
        self.label.setFill(colour)

    def setWidth(self, width):
        "Sets a new width for the button."
        self.rect.setWidth(width)

    def setOutline(self, colour):
        "Sets a new colour for the button's outline."
        self.rect.setOutline(colour)

    def move(self, dx, dy):
        "Sets new coordinates for where the button appears."
        self.xmax += dx
        self.xmin += dx
        self.ymax += dy
        self.ymin += dy
        self.rect.move(dx, dy)
        self.label.move(dx, dy)

    def setFace(self, font):
        "Sets the label's font to a new typeface."
        self.label.setFace(font)

    def setSize(self, fontsize):
        "Sets the label to a new size."
        self.label.setSize(fontsize)

    def setStyle(self, fontstyle):
        "Sets the label to a new style."
        self.label.setStyle(fontstyle)

    def setFontColour(self, colour):
        "Sets the label to a new colour."
        self.label.setFontColour(colour)

    def undraw(self):
        self.rect.undraw()
        self.label.undraw()
        self.deactivate()



class Invisible_Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.label = Text(center, label)
        self.label.setStyle("bold")
        self.label.setSize(30)
        self.label.draw(win)

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def setLabel(self,label):
        "Changes the label string of this button."
        self.label.setText(label)

    def undraw(self):
        self.rect.undraw()
        self.label.undraw()
        self.deactivate()