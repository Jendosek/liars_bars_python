class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.is_alive = True

    def take_turn(self, round_card, view):
        view.show_turn_start(self)
        cards, claimed_count = self.select_cards(round_card, view)
        return cards, claimed_count

    def select_cards(self, round_card, view):
        raise NotImplementedError

    def decide_liar(self, claimed_count, round_card, view):
        raise NotImplementedError

    def remove_cards(self, cards):
        for card in cards:
            self.hand.remove(card)

    def __str__(self):
        return self.name


class HumanPlayer(Player):

    def select_cards(self, round_card, view):
        view.show_hand(self)

        indices = view.ask_card_indices(len(self.hand))
        cards = [self.hand[i] for i in indices]
        claimed_count = len(cards)

        return cards, claimed_count

    def decide_liar(self, claimed_count, round_card, view):
        return view.ask_call_liar(self)


class AIPlayer(Player):
    def __init__(self, name, strategy):
        super().__init__(name)
        self.strategy = strategy

    def select_cards(self, round_card, view):
        cards, claimed_count = self.strategy.choose_cards(self.hand, round_card)
        return cards, claimed_count

    def decide_liar(self, claimed_count, round_card, view):
        return self.strategy.should_call_liar(claimed_count, round_card, self.hand)