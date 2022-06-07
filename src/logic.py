from src.player import Player
from src.deck import Deck
import random


def game_setup(player_one, player_two):
    # Create Players
    player_one = Player(player_one)
    player_two = Player(player_two)

    # Create Deck, shuffle and split it.
    deck = Deck()
    player_one_deck, player_two_deck = deck.split_deck()
    player_one.add_cards(player_one_deck)
    player_two.add_cards(player_two_deck)

    random.shuffle(player_one.all_cards)
    random.shuffle(player_two.all_cards)

    return player_one, player_two


def return_winner(player, rounds):
    print(
        f"{player.name} is the winner 🎉🎉🎉, {player} remaining 🥳 \n{player.name} won in {rounds} rounds"
    )


def play_game(player_one_name: str, player_two_name: str):
    game_on = True
    player_one, player_two = game_setup(player_one_name, player_two_name)
    num_of_rounds = 0

    while game_on:
        num_of_rounds += 1
        print(f"{num_of_rounds}")
        if len(player_one.all_cards) == 0:
            return_winner(player_two, num_of_rounds)
            game_on = False
            break

        if len(player_two.all_cards) == 0:
            return_winner(player_one, num_of_rounds)
            game_on = False
            break

        player_one_hand = []
        player_one_hand.append(player_one.remove_one_card())

        player_two_hand = []
        player_two_hand.append(player_two.remove_one_card())

        war = True

        while war:
            if player_one_hand[-1].value > player_two_hand[-1].value:
                player_one.add_cards(player_one_hand)
                player_one.add_cards(player_two_hand)
                war = False

            elif player_one_hand[-1].value < player_two_hand[-1].value:
                player_two.add_cards(player_one_hand)
                player_two.add_cards(player_two_hand)
                war = False
            else:
                print("WAR HAS STARTED")

                if len(player_one.all_cards) < 5:
                    print(f"{player_one.name} is unable to go to war 😭 ")
                    return_winner(player_two, num_of_rounds)
                    game_on = False
                    break
                elif len(player_two.all_cards) < 5:
                    print(f"{player_two.name} is unable to go to war 😭")
                    return_winner(player_one, num_of_rounds)
                    game_on = False
                    break
                else:
                    for i in range(5):
                        player_one_hand.append(player_one.remove_one_card())
                        player_two_hand.append(player_two.remove_one_card())
