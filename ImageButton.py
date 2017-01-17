# button.py
from graphics import *

class ImageButton:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, image, label):
        """ Creates a rectangular button, eg:
        qb = ImageButton(myWin, centerPoint, image, 'Quit') """
        self.center = center
        self.win = win

        self.rect = Image(center, image)
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.setSize(16)
        self.label.draw(win)
        self.activate()

        w,h = self.rect.getWidth()/2.0, self.rect.getHeight()/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def setFontSize(self, value):
        self.label.setSize(value)

    def setFontColor(self, value):
        self.label.setFill(value)

    def activate(self):
        "Sets this button to 'active'."
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.active = False

    def hide_circle(self):
        self.cover = Image(self.center, "images/hide_circle.png")
        self.cover.draw(self.win)

        self.deactivate()

    def undraw(self):
        try:
            self.cover.undraw()
            self.rect.undraw()
            self.label.undraw()
            self.deactivate()
        except:
            self.rect.undraw()
            self.label.undraw()
            self.deactivate()