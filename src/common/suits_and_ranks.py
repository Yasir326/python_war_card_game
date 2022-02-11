from typing import Tuple, Dict


class SuitsAndRanks:
    def __init__(self):
        self.suits = ("♥", "♠", "♦", "♣")
        self.ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
        self.values = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14,
        }

    def get_suits(self) -> Tuple:
        return self.suits

    def get_ranks(self) -> Tuple:
        return self.ranks

    def get_values(self) -> Dict[str, int]:
        return self.values
