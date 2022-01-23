import unittest
from src.card import Card


class TestCard(unittest.TestCase):
    def test_card_creation(self):
        king_of_spades = Card("♠", "K")
        self.assertEqual(king_of_spades.suit, "♠")
        self.assertEqual(king_of_spades.rank, "K")

    def test_invalid_suit_raises_exception(self):
        with self.assertRaises(Exception) as context:
            Card("Club", "Ace")
        self.assertEqual("Suit must be one of (♠, ♥, ♣, ♦)", str(context.exception))

    def test_invalid_suit_raises_exception(self):
        with self.assertRaises(Exception) as context:
            Card("♠", "Wrong")
        self.assertEqual(
            "Rank must be one of (2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A)",
            str(context.exception),
        )


if __name__ == "main":
    unittest.main()
