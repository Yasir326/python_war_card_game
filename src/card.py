"""
Card class which understands the suit, rank and value
of each card
"""
suits = ("♠", "♥", "♣", "♦")
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
values = {
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


class Card:
    def __init__(self, suit: suits, rank: str):
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


# two_of_clubs = Card("♣", "2")
# three_of_clubs = Card(suits[2], "3")

