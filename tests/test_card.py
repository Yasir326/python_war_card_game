import unittest
from src.card import Card

class TestCard(unittest.TestCase):
    def test_card_creation(self):
        king_of_spades = Card('Spades', 'King')
        self.assertEqual(king_of_spades.suit, 'Spades')
        self.assertEqual(king_of_spades.rank, 'King')


if __name__=='main':
    unittest.main()

