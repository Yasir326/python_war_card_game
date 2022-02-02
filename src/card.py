"""
Card class which understands the suit, rank and value
of each card
"""
from src.common.suits_and_ranks import suits, ranks, values

class Card:
    def __init__(self, suit: str, rank: str):
        if suit not in suits:
            raise Exception("Suit must be one of (♠, ♥, ♣, ♦)")
        self.suit = suit
        if rank not in ranks:
            raise Exception(
                "Rank must be one of (2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A)"
            )
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank}{self.suit}"
