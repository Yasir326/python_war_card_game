"""
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
"""
from src.player import Player
from src.deck import Deck


def game_setup(player_one, player_two) -> None:
    # Create Players
    player_one = Player(player_one)
    player_two = Player(player_two)

    # Create Deck, shuffle and split it.
    deck = Deck()
    deck.shuffle_deck()
    player_one_deck, player_two_deck = deck.split_deck()

    player_one.add_cards(player_one_deck)
    player_two.add_cards(player_two_deck)

    return player_one, player_two


def return_winner(player, rounds) -> None:
    print(
        f"{player.name} is the winner 🎉🎉🎉, {player} remaining 🥳 \n{player.name} won in {rounds} rounds"
    )


def play_game() -> None:
    game_on = True
    player_one, player_two = game_setup("Matt", "Tris")
    num_of_rounds = 0

    while game_on:
        num_of_rounds += 1
        if len(player_one.all_cards) == 0 or len(player_two.all_cards) == 0:
            game_on = False
            if len(player_one.all_cards) > len(player_two.all_cards):
                return_winner(player_one, num_of_rounds)
            else:
                return_winner(player_two, num_of_rounds)
            break

        player_one_card = player_one.remove_one_card()
        player_two_card = player_two.remove_one_card()

        if player_one_card.rank > player_two_card.rank:
            player_one.add_cards(player_two_card)
        else:
            player_two.add_cards(player_one_card)

    # update logic to have an array of cards for each player
    # compare the length of the array to determine the winner

    # add logic for war scenario


play_game()

