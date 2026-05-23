from enum import Enum
import random


class CardType(Enum):
    QUEEN = "Queen"
    KING = "King"
    ACE = "Ace"
    JOKER = "Joker"


class Card:
    def __init__(self, card_type):
        self.card_type = card_type

    def is_joker(self):
        return self.card_type == CardType.JOKER

    def __str__(self):
        return self.card_type.value

    def __repr__(self):
        return f"Card({self.card_type.value})"


class Deck:
    def __init__(self):
        self.cards = []
        self._build()

    def _build(self):
        for card_type in [CardType.QUEEN, CardType.KING, CardType.ACE]:
            for _ in range(6):
                self.cards.append(Card(card_type))
        for _ in range(2):
            self.cards.append(Card(CardType.JOKER))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, count):
        dealt = self.cards[:count]
        self.cards = self.cards[count:]
        return dealt

    def __len__(self):
        return len(self.cards)