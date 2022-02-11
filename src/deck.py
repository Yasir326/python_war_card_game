from importlib_metadata import List
from src.common.suits_and_ranks import SuitsAndRanks
from src.card import Card
import random

suits_and_ranks = SuitsAndRanks()

suits = suits_and_ranks.get_suits()
ranks = suits_and_ranks.get_ranks()


class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle_deck(self) -> None:
        random.shuffle(self.all_cards)

    def deal_card(self) -> Card:
        return self.all_cards.pop()

    def split_deck(self) -> List:
        half = len(self.all_cards)//2
        return self.all_cards[:half], self.all_cards[half:]    
