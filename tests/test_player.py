import unittest
from src.player import Player

class TestDeck(unittest.TestCase):

    def test_player_created(self):
        player_one = Player('Dave')
        self.assertEqual(player_one.name,'Dave')
        self.assertEqual(len(player_one.all_cards), 0)

if __name__ == "main":
    unittest.main()        