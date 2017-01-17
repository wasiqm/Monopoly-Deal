from card import *
from settings import *
import random


class Deck:
    def __init__(self, file):
        """Creates a list of cards from a given file.
        deck = Deck("card_values.txt")"""
        self.file = file
        self.deck = []
        self.settings = Settings("game_settings.txt")

    def create(self):
        """Creates the list of card objects."""
        read_file = open(self.file, "r")
        contents = read_file.readlines()

        for line in contents:
            if line[0] != "#":
                values = line.strip("\n").split("\t")

                if self.settings.access('game_enable_war'):
                    self.deck.append(Card(values))
                else:
                    if values[1] != "armory":
                        self.deck.append(Card(values))

    def add_card(self, card):
        """Adds a card object to the deck list."""
        self.deck.append(card)
        self.shuffle()

    def shuffle(self):
        """Shuffles the card object list."""
        return random.shuffle(self.deck)

    def draw_card(self):
        """Retrieves the first card object in the list and returns it."""
        player_card = self.deck[0]
        self.deck.pop(0)
        return player_card

    def count_cards(self):
        """Returns the amount of cards in the deck."""
        return len(self.deck)

    def print(self):
        """Prints the card name and value."""
        for card in self.deck:
            print(card.get_name(), "$"+card.get_value())

if __name__ == "__main__":
    myDeck = Deck("card_values.txt")
    myDeck.create()
    myDeck.shuffle()
    myDeck.print()
    print(myDeck.count_cards())
