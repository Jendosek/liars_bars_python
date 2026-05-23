# model/strategy.py

import random


class AIStrategy:
    def choose_cards(self, hand, round_card):
        raise NotImplementedError

    def should_call_liar(self, claimed_count, round_card, hand):
        raise NotImplementedError


class AggressiveStrategy(AIStrategy):
    def choose_cards(self, hand, round_card):
        count = min(random.randint(1, 3), len(hand))

        if random.random() < 0.7:
            cards = random.sample(hand, count)
        else:
            valid = [c for c in hand if c.card_type == round_card or c.is_joker()]
            if valid:
                count = min(count, len(valid))
                cards = random.sample(valid, count)
            else:
                cards = random.sample(hand, count)

        return cards, count

    def should_call_liar(self, claimed_count, round_card, hand):
        # Агресор рідко викликає — 25% шанс
        return random.random() < 0.25


class CautiousStrategy(AIStrategy):
    def choose_cards(self, hand, round_card):
        count = min(random.randint(1, 2), len(hand))

        valid = [c for c in hand if c.card_type == round_card or c.is_joker()]
        if valid:
            count = min(count, len(valid))
            cards = random.sample(valid, count)
        else:
            cards = random.sample(hand, count)

        return cards, count

    def should_call_liar(self, claimed_count, round_card, hand):
        return random.random() < 0.55


class AnalystStrategy(AIStrategy):
    def __init__(self):
        self.seen_cards = []

    def choose_cards(self, hand, round_card):
        count = min(random.randint(1, 2), len(hand))

        valid = [c for c in hand if c.card_type == round_card or c.is_joker()]
        if valid:
            count = min(count, len(valid))
            cards = random.sample(valid, count)
        else:
            cards = random.sample(hand, count)

        return cards, count

    def should_call_liar(self, claimed_count, round_card, hand):
        known_count = 0
        for card in hand:
            if card.card_type == round_card:
                known_count += 1
        for card in self.seen_cards:
            if card.card_type == round_card:
                known_count += 1

        remaining = 6 - known_count
        if claimed_count > remaining:
            return True
        if remaining <= 2:
            return random.random() < 0.7
        return random.random() < 0.3

    def remember(self, cards):
        self.seen_cards.extend(cards)

    def reset_memory(self):
        self.seen_cards = []