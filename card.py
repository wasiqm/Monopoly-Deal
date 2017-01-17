from graphics import *
from button import *
from deck import *
import time

class Card:
    def __init__(self, values):
        """Creates a card object. The object can then be used to draw or
        retrieve values from the card.
        card = Card(list)"""

        self.values = values
        self.name = values[0]
        self.type = values[1]
        self.value = values[2]
        self.point = 0

    def get_name(self):
        """Returns the card name."""
        return self.name

    def get_type(self):
        """Returns the type of card."""
        return self.type

    def get_value(self):
        """Returns the value of the card."""
        return self.value

    def get_action(self):
        """Returns what type of action card the card is."""
        return self.values[3]

    def get_point(self):
        """Returns the center point of the card."""
        return self.point

    def get_property_color(self):
        """Returns the property color of the card."""
        return str(self.property_color)

    def set_property_color(self, new_color):
        """Changes the property color of the card."""
        self.property_color = new_color

    def get_rent_colors(self):
        """Returns the rent colors of the card."""
        return (self.values[4].split(","), self.values[5].split(","))

    def get_rent_values(self):
        """Returns the rent values of the card."""
        return self.rentvalues


    def draw(self, win, point):
        """Draws the card to the screen."""
        self.center_x, self.center_y = point.getX(), point.getY()
        self.win = win
        self.point = point

        self.card = Rectangle(Point(self.center_x - 50, self.center_y - 80),
                         Point(self.center_x + 50, self.center_y + 80))

        if self.get_type() == "action" and self.get_action() != "rent":
            self.card.setFill(color_rgb(255, 220, 220))
            self.card.draw(win)

            self.card_border = Rectangle(Point(self.center_x - 40, self.center_y - 70),
                                         Point(self.center_x + 40, self.center_y + 70))
            self.card_border.setOutline(color_rgb(255, 190, 190))
            self.card_border.setWidth(2)
            self.card_border.draw(win)
        elif self.get_type() == "money":
            self.card.setFill(color_rgb(210, 235, 255))
            self.card.draw(win)

            self.card_border = Rectangle(Point(self.center_x - 40, self.center_y - 70),
                                         Point(self.center_x + 40, self.center_y + 70))
            self.card_border.setOutline(color_rgb(190, 215, 255))
            self.card_border.setWidth(2)
            self.card_border.draw(win)
        else:
            self.card.setFill("white")
            self.card.draw(win)

        if self.type != "property":
            if self.type == "action" and self.get_action() == "rent":
                self.primary_rent = self.values[4].split(",")
                pred, pgreen, pblue = self.primary_rent[0], self.primary_rent[1], self.primary_rent[2]

                self.secondary_rent = self.values[5].split(",")
                sred, sgreen, sblue = self.secondary_rent[0], self.secondary_rent[1], self.secondary_rent[2]

                self.first_card_color = Rectangle(Point(self.center_x + 30, self.center_y + 60), Point(self.center_x - 30, self.center_y + 30))
                self.first_card_color.setWidth(0)
                self.first_card_color.setFill(color_rgb(int(pred), int(pgreen), int(pblue)))
                self.first_card_color.draw(self.win)

                self.second_card_color = Rectangle(Point(self.center_x + 30, self.center_y + 30), Point(self.center_x - 30, self.center_y ))
                self.second_card_color.setWidth(0)
                self.second_card_color.setFill(color_rgb(int(sred), int(sgreen), int(sblue)))
                self.second_card_color.draw(self.win)

                self.outside_circle = Circle(Point(self.center_x, self.center_y + 30), 36)
                self.outside_circle.setWidth(10)
                self.outside_circle.setOutline("white")
                self.outside_circle.draw(self.win)

                self.inside_circle = Circle(Point(self.center_x, self.center_y + 30), 15)
                self.inside_circle.setWidth(10)
                self.inside_circle.setOutline("white")
                self.inside_circle.setFill("white")
                self.inside_circle.draw(self.win)

                self.card_name = Text(Point(self.center_x, self.center_y + 30), "Rent")
                self.card_name.setSize(10)
                self.card_name.setStyle("bold")
                self.card_name.draw(self.win)

                self.clean_top = Rectangle(Point(self.center_x - 30, self.center_y + 57),
                                           Point(self.center_x + 30, self.center_y + 61))
                self.clean_top.setFill("white")
                self.clean_top.setWidth(0)
                self.clean_top.draw(self.win)

                self.clean_bottom = Rectangle(Point(self.center_x - 30, self.center_y),
                                           Point(self.center_x + 30, self.center_y + 3))
                self.clean_bottom.setFill("white")
                self.clean_bottom.setWidth(0)
                self.clean_bottom.draw(self.win)

                self.text = Text(Point(self.center_x, self.center_y - 30), "Your opponent must\npay you rent for\nproperties you own\nin these colours.")
                self.text.setSize(7)
                self.text.draw(self.win)

                self.card_type = Text(Point(self.center_x, self.center_y - 70), self.type + " card")
                self.card_type.setSize(8)
                self.card_type.draw(win)

                self.card_value = Text(Point(self.center_x - 35, self.center_y + 70), str(self.value) + "M")
                self.card_value.draw(win)
            else:
                self.card_name = Text(point, self.name)
                self.card_name.setSize(10)
                self.card_name.draw(win)

                self.card_type = Text(Point(self.center_x, self.center_y - 70), self.type + " card")
                self.card_type.setSize(8)
                self.card_type.draw(win)

                self.card_value = Text(Point(self.center_x - 35, self.center_y + 70), str(self.value) + "M")
                self.card_value.draw(win)

        else:
            if self.values[3] != "wild":
                self.property_color = self.values[3].split(",")
                self.rentvalues = [self.values[4], self.values[5], self.values[6]]

                red, green, blue = self.property_color[0], self.property_color[1], self.property_color[2]

                self.card_color = Rectangle(Point(self.center_x + 47, self.center_y + 77), Point(self.center_x - 47, self.center_y + 50))
                self.card_color.setFill(color_rgb(int(red), int(green), int(blue)))
                self.card_color.draw(self.win)

                self.text = Text(Point(self.center_x, self.center_y), "")
                self.text.setSize(8)
                self.text.draw(self.win)

                self.card_name = Text(Point(self.center_x, self.center_y + 64), self.name.rstrip(" "))
                self.card_name.setSize(11)
                self.card_name.draw(win)
            else:
                self.rentvalues = [self.values[4], self.values[5], self.values[6]]
                self.card_color = Image(Point(self.center_x, self.center_y + 63.5), "Images/wildcard_img.png")
                self.card_color.draw(self.win)

                self.text = Text(Point(self.center_x, self.center_y), "This card may\nbe used on any\nset of properties")
                self.text.setSize(8)
                self.text.draw(self.win)

                self.card_name = Text(Point(self.center_x, self.center_y + 64), self.name.rstrip(" "))
                self.card_name.setSize(11)
                self.card_name.setFill("white")
                self.card_name.setStyle("bold")
                self.card_name.draw(win)

            self.card_type = Text(Point(self.center_x + 3, self.center_y - 70), "worth " + self.value + "M")
            self.card_type.setSize(8)
            self.card_type.draw(win)

            box_yloc = 30
            self.rent_values = []

            for i in range(3):
                if self.rentvalues[i] != "n/a":
                    self.rent_values.append(Rectangle(Point(self.center_x - 40, self.center_y + box_yloc),Point(self.center_x - 25, self.center_y + box_yloc - 15)))
                    self.rent_values.append(Text(Point(self.center_x - 32, self.center_y + box_yloc - 7.5), i+1, 8))
                    self.rent_values.append(Text(Point(self.center_x + 25, self.center_y + box_yloc - 7.5), self.rentvalues[i] + "M", 10))
                    self.rent_values.append(Text(Point(self.center_x-4, self.center_y + box_yloc - 5), "."*11, 8))

                    if i == 2:
                        self.rent_values.append(Text(Point(self.center_x-4, self.center_y + box_yloc - 3), "Full set", 6))
                    elif i == 1 and self.rentvalues[2] == "n/a":
                        self.rent_values.append(Text(Point(self.center_x-4, self.center_y + box_yloc - 3), "Full set", 6))

                    box_yloc -= 25

            for i in self.rent_values:
                i.draw(win)

    def draw_buttons(self):
        """Draws the buttons associated with the card."""
        if self.get_type() == "action":
            self.use_card = Button(self.win, Point(self.center_x - 28, self.center_y + 95), 45, 20, "Use")
            self.use_card.activate()

            self.add_bank = Button(self.win, Point(self.center_x + 28, self.center_y + 95), 45, 20, "Bank")
            self.add_bank.activate()

            return self.use_card, self.add_bank

        elif self.get_type() == "money":
            self.add_bank = Button(self.win, Point(self.center_x, self.center_y + 95), 100, 20, "Bank")
            self.add_bank.activate()

            return self.add_bank

        elif self.get_type() == "property":
            self.use_card = Button(self.win, Point(self.center_x, self.center_y + 95), 100, 20, "Use")
            self.use_card.activate()

            return self.use_card

    def deactivate_buttons(self):
        """Disables the buttons for the card."""
        if self.get_type() == "action":
            self.use_card.deactivate()
            self.add_bank.deactivate()
        elif self.get_type() == "money":
            self.add_bank.deactivate()
        elif self.get_type() == "property":
            self.use_card.deactivate()

    def undraw_buttons(self):
        """Undraws the buttons of the card."""
        if self.get_type() == "action":
            self.use_card.undraw()
            self.add_bank.undraw()
        elif self.get_type() == "money":
            self.add_bank.undraw()
        elif self.get_type() == "property":
            self.use_card.undraw()

    def undraw(self):
        """Undraws the card."""
        if self.type != "property":
            self.card.undraw()
            self.card_name.undraw()
            self.card_type.undraw()
            self.card_value.undraw()

            if self.type == "action" and self.get_action() != "rent":
                self.card_border.undraw()
            elif self.type == "action" and self.get_action() == "rent":
                self.first_card_color.undraw()
                self.second_card_color.undraw()
                self.inside_circle.undraw()
                self.outside_circle.undraw()
                self.clean_top.undraw()
                self.clean_bottom.undraw()
                self.text.undraw()

            elif self.type != "action":
                self.card_border.undraw()
        else:
            self.card.undraw()
            self.card_name.undraw()
            self.card_color.undraw()
            self.card_type.undraw()
            self.text.undraw()

            for i in self.rent_values:
                i.undraw()

if __name__ == "__main__":
    win = GraphWin("Card", 1000, 500)
    win.setCoords(0, 0, 1000, 500)

    myDeck = Deck("card_values.txt")
    myDeck.create()
    myDeck.shuffle()

    cards = []

    for i in range(7):
        cards.append(myDeck.draw_card())

    x = 100

    for card in cards:
        card.draw(win, Point(x, 250))
        card.draw_buttons()
        x += 135

    win.getMouse()