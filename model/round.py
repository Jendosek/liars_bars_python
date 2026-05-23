import random
from model.card import CardType, Deck

class Round:
    def __init__(self, players):
        self.players = [p for p in players if p.is_alive]
        self.round_card = self._pick_round_card()
        self.table = []
        self.current_index = 0
        self.deck = Deck()
        self.deck.shuffle()
        self._deal_cards()

    def _pick_round_card(self):
        return random.choice([CardType.QUEEN, CardType.KING, CardType.ACE])

    def _deal_cards(self):
        cards_per_player = 5
        for player in self.players:
            player.hand = self.deck.deal(cards_per_player)

    def get_current_player(self):
        return self.players[self.current_index]

    def get_next_player(self):
        next_index = (self.current_index + 1) % len(self.players)
        return self.players[next_index]

    def play_cards(self, cards):
        self.table.extend(cards)

    def check_liar(self, cards):
        for card in cards:
            if card.card_type != self.round_card and not card.is_joker():
                return True
        return False

    def advance_turn(self):
        self.current_index = (self.current_index + 1) % len(self.players)