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

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_card(self):
        return self.all_cards.pop()
