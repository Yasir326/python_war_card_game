import unittest
from src.player import Player


class TestDeck(unittest.TestCase):
    def test_player_created(self):
        player_one = Player("Dave")
        self.assertEqual(player_one.name, "Dave")
        self.assertEqual(len(player_one.all_cards), 0)

    def test_add_one_card(self):
        player_one = Player("Dave")
        self.assertEqual(len(player_one.all_cards), 0)
        player_one.add_cards("3♥")
        self.assertEqual(len(player_one.all_cards), 1)
        self.assertEqual(player_one.all_cards[0], "3♥")

    def test_add_list_of_cards(self):
        player_one = Player("Dave")
        self.assertEqual(len(player_one.all_cards), 0)
        player_one.add_cards(["3♥", "2♠", "4♥", "3♠"])
        self.assertEqual(len(player_one.all_cards), 4)

    def test_remove_one_card(self):
        player_one = Player("Dave")
        self.assertEqual(len(player_one.all_cards), 0)
        player_one.add_cards("3♥")
        self.assertEqual(len(player_one.all_cards), 1)
        player_one.remove_one_card()
        self.assertEqual(len(player_one.all_cards), 0)


if __name__ == "main":
    unittest.main()
