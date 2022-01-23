import unittest
from src.deck import Deck

class TestDeck(unittest.TestCase):
    def test_deck_created(self):
        new_deck = Deck()
        self.assertEqual(len(new_deck.all_cards), 52)






if __name__ == "main":
    unittest.main()