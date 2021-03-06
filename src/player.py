from src.card import Card


class Player:
    def __init__(self, name: str):
        self.name = name
        self.all_cards = []

    def remove_one_card(self) -> Card:
        return self.all_cards.pop(0)

    def add_cards(self, new_cards) -> None:
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def name(self) -> str:
        return self.name

    def __str__(self) -> str:
        return f"{self.name} has {len(self.all_cards)} cards"
