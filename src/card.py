from src.common.suits_and_ranks import SuitsAndRanks

suits_and_ranks = SuitsAndRanks()

suits = suits_and_ranks.get_suits()
ranks = suits_and_ranks.get_ranks()
values = suits_and_ranks.get_values()


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
