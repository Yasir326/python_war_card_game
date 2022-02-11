'''
1. Create two instances of player class
2. Create instance of a new deck 
3. Shuffle Deck
4. Split Deck
5. Check if somebody has lost? check length of player hand
6. Game can continue playing game on, break out of loop if player has lost
7. Each player draws a card 
8. do a comparison against the cards in
9. Player with higher card takes all the cards and
10. If draw (war) player draw additional 3 cards
11. Create while at War loop Card 
12. Break out of loop when War ended
13. Check if player has lost.
14. announce if player has won.
'''
from src.player import Player
from src.deck import Deck

player_one = Player('Matt')
player_two = Player('Tris')

deck = Deck()
deck.shuffle_deck()

player_one_deck, player_two_deck = deck.split_deck()








