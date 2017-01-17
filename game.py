
import time
from graphics import *
from button import Button
from deck import *
from card import *
from player import *
from settings import *


class GraphicsInterface:
    """The graphical user interface for the user to interact with and the
    implementation of all of the elements of the game.
    gui = GraphicsInterface(self.win)"""

    def __init__(self, win):
        """Constructs the instance variables and the GUI required for the
        game to run"""
        self.winner = False
        # Create a window with width = 360 and height = 240
        self.win = win

        # Get setting and set the background
        self.settings = Settings("game_settings.txt")
        self.win.setBackground("maroon")
        #self.background = Image(Point(512, 325), "Images/temp_background.png")
        #self.background.draw(self.win)

        # Draw buttons to submit the user input
        self.quitButton = Button(self.win, Point(90, 440), 100, 30, "Quit")
        self.quitButton.activate()

        self.NextTurnButton = Button(self.win, Point(915, 440), 100, 30,
                                     "Next Turn")
        self.NextTurnButton.activate()

        self.bank_area_player = Image(Point(90, 330), "Images/bank_area.png")
        self.bank_area_player.draw(self.win)
        self.money_circle_player = Circle(Point(90, 365), 20)
        self.money_circle_player.setFill("green")
        self.money_circle_player.draw(self.win)

        self.bank_area_opposing = Image(Point(915, 550), "Images/bank_area.png")
        self.bank_area_opposing.draw(self.win)
        self.money_circle_opposing = Circle(Point(915, 585), 20)
        self.money_circle_opposing.setFill("green")
        self.money_circle_opposing.draw(self.win)

        self.money_player = Text(Point(90, 365), '0M')
        self.money_player.draw(self.win)
        self.money_opposing = Text(Point(915, 585), '0M')
        self.money_opposing.draw(self.win)

        self.last_action = Text(Point(512, 430), "")
        self.last_action.setSize(12)
        self.last_action.draw(self.win)

        self.line = Line(Point(1000, 420), Point(0, 420))
        self.line.setWidth(2)
        self.line.draw(self.win)

        self.turn = 0
        self.game_deck = Deck("card_values.txt")
        self.game_deck.create()
        self.game_deck.shuffle()
        
        self.player1 = Player("player1")
        self.player2 = Player("player2")

        self.cards_in_deck = Text(Point(915, 410), "Cards in deck: " +
                                  str(self.game_deck.count_cards()))
        self.cards_in_deck.setSize(10)
        self.cards_in_deck.draw(self.win)

    def update_player_country(self, player, replacewith, image):
        """Changes the players' country flag icon on the GUI corresponding to
        which player's turn it is and what country they had chosen"""
        if player == 1:
            self.player1.update_country(replacewith)
            self.player1.update_flag(image)
        elif player == 2:
            self.player2.update_country(replacewith)
            self.player2.update_flag(image)

    def turn_player(self):
        """Returns the player object of the player whose turn it currently is"""
        if self.turn % 2 == 0:
            return self.player2
        else:
            return self.player1

    def opposite_turn(self):
        """Returns the player object of the player
        whose turn it currently is not"""
        if self.turn % 2 == 0:
            return self.player1
        else:
            return self.player2

    def hide_card_buttons(self, card):
        """Deactivates a card's corresponding
        buttons and draws over draws over them"""
        card.deactivate_buttons()
        hider = Rectangle(Point(card.get_point().getX() - 52,
                    card.get_point().getY() + 110),
                Point(card.get_point().getX() + 52,
                    card.get_point().getY() + 85,))

        hider.setFill("maroon")
        hider.setOutline("maroon")
        hider.draw(self.win)

    def show_hand(self):
        """Displays the turn player's hand on the GUI, with the positioning of
        the cards dependent on how many cards there are in the player's hand"""
        increment_amount = 400
        if len(self.turn_player().get_hand()) == 1:
            card_x = 500
        elif len(self.turn_player().get_hand()) == 2:
            card_x = 350
        elif len(self.turn_player().get_hand()) == 3:
            increment_amount = 200
            card_x = 250
        elif len(self.turn_player().get_hand()) == 4:
            increment_amount = 170
            card_x = 240
        elif len(self.turn_player().get_hand()) == 5:
            increment_amount = 150
            card_x = 200
        elif len(self.turn_player().get_hand()) == 6:
            increment_amount = 140
            card_x = 150
        elif len(self.turn_player().get_hand()) == 7:
            increment_amount = 130
            card_x = 115
        else:
            increment_amount = 120
            card_x = 90

        self.card_buttons = {}
        for card in self.turn_player().get_hand():
            card.draw(self.win, Point(card_x, 90))
            if type(card.draw_buttons()) == tuple:
                self.card_buttons.update({card.draw_buttons()[0]:card})
                self.card_buttons.update({card.draw_buttons()[1]:card})
            else:
                self.card_buttons.update({card.draw_buttons():card})
            card_x += increment_amount

    def find_full_sets(self, player):
        """Returns all of the sets (all properties of a certain color) a
        player has in their properties"""
        player.get_properties().sort(key=Card.get_property_color)

        full_sets = []
        card_set = []
        count = 1
        for card2 in player.get_properties():
            if count > 1:
                if len(card_set) == 0:
                    if card2.get_property_color() == \
                    previous_card.get_property_color():
                        card_set.append(previous_card)
                        card_set.append(card2)
                        if card_set[0].get_property_color()\
                                == "['40', '78', '161']"\
                                or card_set[0].get_property_color()\
                                == "['89', '12', '56']":
                            if card_set not in full_sets:
                                full_sets.append(card_set)
                            card_set = []
                            count = 0

                elif card2.get_property_color() == \
                        card_set[0].get_property_color():
                    if card_set not in full_sets:
                        while len(card_set) >= 4:
                            for possible_territory in card_set:
                                if possible_territory.get_name == "Territory":
                                    self.turn_player().hand_add\
                                        (possible_territory)
                                    self.turn_player().properties_subtract\
                                        (possible_territory)
                                    card_set.remove(possible_territory)
                                    break

                        if card_set[0].get_property_color()\
                                == "['40', '78', '161']"\
                                or card_set[0].get_property_color()\
                                == "['89', '12', '56']":
                            while len(card_set) >= 3:
                                for possible_territory in card_set:
                                    if possible_territory.get_name ==\
                                            "Territory":
                                        self.turn_player().hand_add\
                                            (possible_territory)
                                        self.turn_player().properties_subtract\
                                            (possible_territory)
                                        card_set.remove(possible_territory)
                                        break

                        card_set.append(card2)
                        full_sets.append(card_set)
                        card_set = []
                        count = 0

                else:
                    card_set = []
                    count = 0
            previous_card = card2
            count += 1

        return full_sets

    def hide_hand(self):
        """Removes the turn player's hand from the GUI,
         undrawing each of the cards"""
        for card in self.turn_player().get_hand():
            self.hide_card_buttons(card)
            card.undraw()

    def show_properties(self, player, card_y):
        """Displays a player's properties on the GUI, with the positioning of
        the cards dependent on how many cards there are in the player's
        properties and whose turn it is"""
        self.cards_in_deck.setText("Cards in deck: " +
                                   str(self.game_deck.count_cards()))
        increment_amount = 300
        repeats = 0
        seen_colors = []
        for card in player.get_properties():
            if card.get_property_color() in seen_colors:
                #if str(seen_colors).count(card.get_property_color()) >= 1:
                repeats += 1
            seen_colors.append(card.get_property_color())

        if len(player.get_properties()) - repeats == 1:
            card_x = 500
        elif len(player.get_properties()) - repeats == 2:
            card_x = 350
        elif len(player.get_properties()) - repeats == 3:
            increment_amount = 200
            card_x = 250
        elif len(player.get_properties()) - repeats == 4:
            increment_amount = 170
            card_x = 230
        elif len(player.get_properties()) - repeats == 5:
            increment_amount = 140
            card_x = 215
        elif len(player.get_properties()) - repeats == 6:
            increment_amount = 110
            card_x = 210
        elif len(player.get_properties()) - repeats == 7 and card_y == 550:
            increment_amount = 105
            card_x = 100
        elif len(player.get_properties()) - repeats == 7 and card_y == 330:
            increment_amount = 105
            card_x = 205
        elif len(player.get_properties()) - repeats == 8 and card_y == 550:
            increment_amount = 103
            card_x = 100
        elif len(player.get_properties()) - repeats == 8 and card_y == 330:
            increment_amount = 103
            card_x = 202

        seen_colors = {}
        for card in player.get_properties():
            if card.get_property_color() in seen_colors:
                if card.get_property_color() + "times 2" in seen_colors:
                    card.draw(self.win, Point
                    (seen_colors[card.get_property_color()].get_point().getX(),
                     card_y - 52))
                else:
                    card.draw(self.win, Point
                    (seen_colors[card.get_property_color()].get_point().getX(),
                     card_y - 26))
                    seen_colors.update({card.get_property_color()
                                        + "times 2": card})
            else:
                card.draw(self.win, Point(card_x, card_y))
                card_x += increment_amount
                seen_colors.update({card.get_property_color():card})

    def undraw_cards(self, list_of_cards):
        """Undraws each card from a list"""
        for card in list_of_cards:
            card.undraw()

    def update_money(self):
        """Projects a player's money on the GUI corresponding with
        which player's turn it is and how much money they have"""
        self.money_player.setText(
            str(self.turn_player().get_treasury_value()) + 'M')
        self.money_opposing.setText(
            str(self.opposite_turn().get_treasury_value()) + 'M')

    def use_card(self, action, card):
        """Implements the effect of a card's button click, with the effect
        varying drastically depending on what card and button was clicked"""

        self.cards_in_deck.setText("Cards in deck: " +
                                   str(self.game_deck.count_cards()))
        if action == "Bank":
            self.hide_card_buttons(card)
            self.turn_player().hand_subtract(card)
            self.turn_player().treasury_add(card.get_value())
            self.update_money()

        elif card.type == "action":
            if not self.opposite_turn().just_say_no_status():
                if card.get_action() == "takemoney":
                    self.hide_card_buttons(card)
                    self.turn_player().hand_subtract(card)
                    
                    self.game_deck.add_card(card)
                    self.opposite_turn().take_money(5, self.turn_player())
                    self.undraw_cards(self.turn_player().get_properties())
                    self.undraw_cards(self.opposite_turn().get_properties())
                    self.show_properties(self.turn_player(), 330)
                    self.show_properties(self.opposite_turn(), 550)
                    self.update_money()
                    self.last_action.setText(self.turn_player().get_country() +
                                             " stole 5M!")

                elif card.get_action() == "no":
                    if not self.turn_player().just_say_no_status():
                        self.hide_card_buttons(card)
                        self.turn_player().hand_subtract(card)
                        
                        self.game_deck.add_card(card)
                        self.turn_player().set_just_say_no(True)
                        self.last_action.setText(self.turn_player().get_country
                                                 () + " used a Veto card!")

                elif card.get_action() == "birthday":
                    self.hide_card_buttons(card)
                    self.turn_player().hand_subtract(card)
                    self.game_deck.add_card(card)
                    self.opposite_turn().take_money(2, self.turn_player())
                    self.undraw_cards(self.turn_player().get_properties())
                    self.undraw_cards(self.opposite_turn().get_properties())
                    self.show_properties(self.turn_player(), 330)
                    self.show_properties(self.opposite_turn(), 550)
                    self.update_money()
                    if len(self.turn_player().get_hand()) < 8:
                        self.hide_hand()
                        self.turn_player().hand_add(self.game_deck.draw_card())
                        self.show_hand()
                        self.check_winner()
                    self.last_action.setText(self.turn_player().get_country() +
                                             " celebrated a national holiday!")

                elif card.get_action() == "draw":
                    self.hide_card_buttons(card)
                    self.turn_player().hand_subtract(card)
                    self.game_deck.add_card(card)
                    self.hide_hand()
                    for i in range(2):
                        if len(self.turn_player().get_hand()) < 8:
                            self.turn_player().hand_add\
                                (self.game_deck.draw_card())
                            self.check_winner()
                    self.show_hand()
                    self.last_action.setText(self.turn_player().get_country() +
                                             " had an economic boom!")

                elif card.get_action() == "steal1":
                    if len(self.opposite_turn().get_properties()) > 0:
                        self.hide_card_buttons(card)
                        self.turn_player().hand_subtract(card)
                        self.game_deck.add_card(card)

                        if self.opposite_turn().get_properties()[0].get_name\
                                == "Territory":
                            self.turn_player().hand_add\
                                (self.opposite_turn().get_properties()[0])
                        else:
                            self.turn_player().properties_add\
                                (self.opposite_turn().get_properties()[0])

                        self.opposite_turn().properties_subtract\
                            (self.turn_player().get_properties()[-1])
                        self.undraw_cards(self.turn_player().get_properties())
                        self.undraw_cards(self.opposite_turn().get_properties())
                        self.show_properties(self.turn_player(), 330)
                        self.show_properties(self.opposite_turn(), 550)
                        self.last_action.setText(self.turn_player().get_country
                                                 () + " stole a property card!")

                elif card.get_action() == "steal3":
                    self.opposite_turn().get_properties().sort\
                    (key=Card.get_property_color)
                    full_sets = self.find_full_sets(self.opposite_turn())

                    if len(full_sets) > 0:
                        self.hide_card_buttons(card)
                        self.turn_player().hand_subtract(card)
                        self.game_deck.add_card(card)

                        for i in range(0, 3):
                            if full_sets[0][0].get_property_color() == \
                            "['89', '12', '56']" or full_sets[0][0].\
                            get_property_color() == "['40', '78', '161']":
                                if i == 2:
                                    break
                            self.turn_player().properties_add\
                                (full_sets[0][-i])
                            self.opposite_turn().properties_subtract\
                                (full_sets[0][-i])
                            self.undraw_cards\
                                (self.turn_player().get_properties())
                            self.undraw_cards\
                                (self.opposite_turn().get_properties())
                            self.show_properties(self.turn_player(), 330)
                            self.show_properties(self.opposite_turn(), 550)
                        self.last_action.setText(self.turn_player().get_country
                                                 () + " stole an entire set!")
                    else:
                        self.hide_card_buttons(card)
                        self.turn_player().hand_subtract(card)
                        self.game_deck.add_card(card)

                elif card.get_action() == "trade":
                    if len(self.turn_player().get_properties()) > 0 and \
                            len(self.opposite_turn().get_properties()) > 0:

                        player_card = self.turn_player().get_properties()[-1]
                        opponent_card = \
                            self.opposite_turn().get_properties()[-1]

                        self.hide_card_buttons(card)
                        self.turn_player().hand_subtract(card)
                        self.game_deck.add_card(card)

                        if opponent_card.get_name == "Territory":
                            self.turn_player().hand_add(opponent_card)
                        else:
                            self.turn_player().properties_add(opponent_card)

                        if player_card.get_name == "Territory":
                            self.opposite_turn().hand_add(player_card)
                        else:
                            self.opposite_turn().properties_add(player_card)

                        self.turn_player().properties_subtract(player_card)
                        self.opposite_turn().properties_subtract(opponent_card)

                        self.undraw_cards(self.turn_player().get_properties())
                        self.undraw_cards(self.opposite_turn().get_properties())
                        self.show_properties(self.turn_player(), 330)
                        self.show_properties(self.opposite_turn(), 550)
                        self.last_action.setText\
                            (self.turn_player().get_country() +
                             " swapped a property card!")

                elif card.get_action() == "doublerent":
                    self.hide_card_buttons(card)
                    self.turn_player().hand_subtract(card)
                    self.game_deck.add_card(card)
                    self.turn_player().set_double_rent(True)
                    self.last_action.setText(self.turn_player().get_country() +
                                             " doubled their next rent cost.")

                elif card.get_action() == "rent":
                    if len(self.turn_player().get_properties()) > 0:
                        action = True
                        self.game_deck.add_card(card)
                        self.hide_card_buttons(card)
                        self.turn_player().hand_subtract(card)

                        property_color1 = str(card.get_rent_colors()[0])
                        property_color2 = str(card.get_rent_colors()[1])
                        property_count1 = 0
                        property_count2 = 0

                        pay_total = 0
                        for card in self.turn_player().get_properties():
                            if card.get_name() == "Territory":
                                pay_total += 1
                            elif card.get_property_color() == property_color1:
                                pay_total +=\
                                    int(card.get_rent_values()[property_count1])
                                property_count1 += 1
                            elif card.get_property_color() == property_color2:

                                pay_total += \
                                    int(card.get_rent_values()[property_count2])
                                property_count2 += 1

                        if self.turn_player().double_rent_status():
                            pay_total *= 2
                            self.turn_player().set_double_rent(False)

                        self.opposite_turn().take_money\
                        (pay_total, self.turn_player())
                        self.undraw_cards(self.turn_player().get_properties())
                        self.undraw_cards(self.opposite_turn().get_properties())
                        self.show_properties(self.turn_player(), 330)
                        self.show_properties(self.opposite_turn(), 550)
                        self.update_money()
                        self.last_action.setText(self.turn_player().get_country
                                                 () + " used a rent card!")

            else:
                self.hide_card_buttons(card)
                veto_text = Text(Point(500, 325), "Vetoed!")
                veto_text.setSize(28)
                veto_text.draw(self.win)
                time.sleep(1)
                veto_text.undraw()
                self.game_deck.add_card(card)
                self.opposite_turn().set_just_say_no(False)
                self.turn_player().hand_subtract(card)

        else:
            if card.get_name() == "Territory" and\
                            len(self.turn_player().get_properties()) > 0:
                if len(self.find_full_sets(self.turn_player())) > 0:
                    done = False
                    for property in self.turn_player().get_properties():
                        for set in self.find_full_sets(self.turn_player()):
                            if property not in set:
                                card.set_property_color\
                                    (property.get_property_color())
                                self.hide_card_buttons(card)
                                self.turn_player().properties_add(card)
                                self.turn_player().hand_subtract(card)
                                self.undraw_cards\
                                    (self.turn_player().get_properties())
                                self.show_properties(self.turn_player(), 330)
                                done = True
                                break
                        if done:
                            break
                else:
                    card.set_property_color(self.turn_player(
                    ).get_properties()[0].get_property_color())
                    self.hide_card_buttons(card)
                    self.turn_player().properties_add(card)
                    self.turn_player().hand_subtract(card)
                    self.undraw_cards(self.turn_player().get_properties())
                    self.show_properties(self.turn_player(), 330)

            elif card.get_name() != "Territory":
                for set in self.find_full_sets(self.turn_player()):
                    if set[0].get_property_color() == card.get_property_color():
                        for possible_wild in set:
                            if possible_wild.get_name() == "Territory":
                                self.turn_player().hand_add(possible_wild)
                                self.turn_player().\
                                    properties_subtract(possible_wild)
                self.hide_card_buttons(card)
                self.turn_player().properties_add(card)
                self.turn_player().hand_subtract(card)
                self.undraw_cards(self.turn_player().get_properties())
                self.show_properties(self.turn_player(), 330)

    def check_winner(self):
        """Checks to see if a player has won by checking the two possible win
        conditions (hitting 50M or by having three full sets) and then sets
        the winner instance variable accordingly"""
        win_text = Text(Point(500, 325), "")

        if self.turn_player().get_treasury_value() >= \
                self.settings.access('win_max_money') \
                and self.settings.access('win_by_money'):
            win_text = Text(Point(500, 325), str(self.turn_player(
            ).get_country()) + " wins by hitting max money!")
            self.winner = True
            time.sleep(2)

        elif len(self.find_full_sets(self.turn_player())) >= 3:
            win_text = Text(Point(500, 325),  str(self.turn_player(
            ).get_country()) + " wins by having three full sets!")
            self.winner = True
            time.sleep(2)

        elif len(self.find_full_sets(self.opposite_turn())) >= 3:
            win_text = Text(Point(500, 325),  str(self.opposite_turn(
            ).get_country()) + " wins by having three full sets!")
            self.winner = True
            time.sleep(2)

        win_text.setSize(28)
        win_text.draw(self.win)
        self.cards_in_deck.setText("Cards in deck: " +
                                   str(self.game_deck.count_cards()))

    def run(self):
        """Runs the game by going through each step of a player's turn and
        then switching over to the next player's turn"""
        activities = 3
        pt = Point(915, 440)

        while not self.winner:
            self.cards_in_deck.setText("Cards in deck: " +
                                       str(self.game_deck.count_cards()))
            self.check_winner()
            if self.NextTurnButton.clicked(pt) or activities == 0 or \
                    len(self.turn_player().get_hand()) == 0:
                self.check_winner()
                if self.turn != 0:
                    player_flag.undraw()
                    opponent_flag.undraw()

                self.hide_hand()
                activities = 3
                self.check_winner()
                self.turn += 1

                player_flag = Image(Point(89, 280),
                                    self.turn_player().get_flag())
                player_flag.draw(self.win)

                opponent_flag = Image(Point(915, 500),
                                      self.opposite_turn().get_flag())
                opponent_flag.draw(self.win)

                self.update_money()

                if self.turn > 1:
                    #self.undraw_cards(self.opposite_turn().get_hand())
                    self.hide_hand()
                    self.undraw_cards(self.opposite_turn().get_properties())
                    self.undraw_cards(self.turn_player().get_properties())

                    self.show_properties(self.turn_player(), 330)
                    self.show_properties(self.opposite_turn(), 550)

                if self.turn <= 2:
                    for i in range(self.settings.access("player_start_cards")):
                        self.turn_player().hand_add(self.game_deck.draw_card())
                    self.show_hand()
                    time.sleep(1)
                    self.hide_hand()

                for i in range(2):
                    if len(self.turn_player().get_hand()) < 8:
                        self.turn_player().hand_add\
                            (self.game_deck.draw_card())
                        self.check_winner()

                self.show_hand()

                # Check for button clicks

            elif self.quitButton.clicked(pt):
                self.win.close()
                break

            pt = self.win.getMouse()
            for button in self.card_buttons:
                self.check_winner()
                if button.clicked(pt):
                    self.use_card(button.getLabel(), self.card_buttons[button])
                    activities -= 1
                    break
            self.check_winner()

        # Close window
        time.sleep(1)
        self.win.close()
