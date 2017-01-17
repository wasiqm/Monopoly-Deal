
from card import *


class Player:
    """Represents one of the two players of the game, holding all of that
    player's in-game information (like how much money/properties they have)
    self.player1 = Player('player1')"""

    def __init__(self, name):
        """Constructs the starting values for the player"""
        self.name = name
        self.treasury = 0
        self.properties = []
        self.hand = []
        self.just_say_no = False
        self.double_rent = False
        self.country = ""
        self.flag = ""

    def just_say_no_status(self):
        """Returns whether or not a 'just say no'/'veto'
        card still has an active use for the player"""
        return self.just_say_no

    def set_just_say_no(self, boolean):
        """Activates or deactivates the effect of a 'just say no'/'veto' card"""
        self.just_say_no = boolean

    def double_rent_status(self):
        """Returns whether or not a 'double tariffs'
        card still has an active use for the player"""
        return self.double_rent

    def set_double_rent(self, boolean):
        """Activates or deactivates the effect of a 'double tariffs' card"""
        self.double_rent = boolean

    def update_country(self, country):
        """Updates the country that the player represents"""
        self.country = country

    def update_flag(self, flag):
        """Updates the country flag that corresponds to the player"""
        self.flag = flag

    def get_country(self):
        """Returns the country that the player represents"""
        return self.country

    def get_flag(self):
        """Returns the country flag that corresponds to the player"""
        return self.flag

    def get_hand(self):
        """Returns the list of cards that represent the player's hand"""
        return self.hand

    def hand_add(self, new_card):
        """Adds a new card to the player's hand"""
        self.hand.append(new_card)

    def hand_subtract(self, dead_card):
        """Removes a card from the player's hand"""
        self.hand.remove(dead_card)
        dead_card.undraw_buttons()
        dead_card.undraw()

    def get_properties(self):
        """Returns the list of cards that represent the player's properties"""
        return self.properties

    def properties_add(self, card):
        """Adds a new card to the player's properties"""
        self.properties.append(card)

    def properties_subtract(self, card):
        """Removes a card from the player's properties"""
        self.properties.remove(card)

    def get_treasury_value(self):
        """Returns the integer that represents the cash in the
        player's treasury"""
        return self.treasury

    def treasury_add(self, value):
        """Adds money to the player's treasury"""
        self.treasury += int(value)

    def treasury_subtract(self, value):
        """Takes away money from the player's treasury"""
        self.treasury -= int(value)

    def take_money(self, value, turn_player):
        """Takes away money from the player's treasury and adds it the the
        treasury of the turn player, and if there isn't enough money to give
        away, gives the corresponding number of properties away based on
        value"""
        self.treasury -= value
        turn_player.treasury_add(value)
        if self.treasury < 0:
            debt = self.treasury * -1
            self.treasury = 0
            turn_player.treasury_subtract(debt)
            self.properties.sort(key=Card.get_value)
            while debt > 0 and len(self.properties) != 0:
                debt -= int(self.properties[0].get_value())
                if self.properties[0].get_name == "Territory":
                    turn_player.hand_add(self.properties[0])
                else:
                    turn_player.properties_add(self.properties[0])
                self.properties_subtract(turn_player.get_properties()[-1])
