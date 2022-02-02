"""
Instantiate new Deck
    1. Create all 52 cards
    2. Hold as a list of card objects
Shuffle Deck through method call
    1. Random Library shuffle function
Deal cards from the Deck
    pop method from card list.
"""
from src.common.suits_and_ranks import suits, ranks
from src.card import Card
import random


class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop()


        
            


  




