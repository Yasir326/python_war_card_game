"""
1. This class will be used to hold a player's current list of cards
2. A player should be able to add or remove cards from their hand (list of card objects)
3. Player should be able to add a single card or multiple cards to their list
Translate a deck of cards with a top and bottom, to a Python list.
"""


class Player:
    def __init__(self, name: str):
        self.name = name
        self.all_cards = []

    def remove_one_card(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)    

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"
