import unittest
from src.deck import Deck


class TestDeck(unittest.TestCase):
    def test_deck_created(self):
        new_deck = Deck()
        self.assertEqual(len(new_deck.all_cards), 52)

    def test_first_card(self):
        new_deck = Deck()
        self.assertEqual(str(new_deck.all_cards[0]), "2♥")

    def test_last_card(self):
        new_deck = Deck()
        self.assertEqual(str(new_deck.all_cards[-1]), "A♣")

    def test_deck_is_shuffled(self):
        new_deck = Deck()
        new_deck.shuffle_deck()
        self.assertNotEqual(str(new_deck.all_cards[0]), "2♥")
        self.assertNotEqual(str(new_deck.all_cards[-1]), "A♣")

    def test_deal(self):
        new_deck = Deck()
        card = new_deck.deal_card()
        self.assertEqual(str(card), "A♣")
        self.assertEqual(len(new_deck.all_cards), 51)

    def test_split_deck(self):
        new_deck = Deck()
        player_one_deck, player_two_deck = new_deck.split_deck()
        self.assertEqual(len(player_one_deck), 26)
        self.assertEqual(len(player_two_deck), 26)


if __name__ == "main":
    unittest.main()
