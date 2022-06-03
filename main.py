from src.logic import play_game
import time


def countdown(t):
    sleep = time.sleep(1)
    while t > 0:
        print(f"GAME STARTING IN {t} ⏰ ")
        t -= 1
        time.sleep(1)


if __name__ == "__main__":

    player_one = input("Please enter the name for Player One: ")
    player_two = input("Please enter the name for Player Two: ")
    countdown(3)
    print("GAME STARTING 🚀🚀🚀")
    try:
        play_game(player_one, player_two)
    except Exception as e:
        print(f"Print something went wrong due to {e}")
    else:
        print(f"GAME OVER 🏁 Thanks for playing {player_one} & {player_two} 🤗")
