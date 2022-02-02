'''
1. This class will be used to hold a player's current list of cards
2. A player should be able to add or remove cards from their hand (list of card objects)
3. Player should be able to add a single card or multiple cards to their list
Translate a deck of cards with a top and bottom, to a Python list.
'''
class Player:

    def __init__(self, name:str):
        self.name = name
        self.all_cards = []

    def remove_one_card(self):
        pass

    def add_cards(self):
        pass