import random
from model.player import AIPlayer
from model.strategy import AggressiveStrategy, CautiousStrategy, AnalystStrategy


class PlayerFactory:

    NAMES = [
        "Loshok", "Yura", "Zenya", "Sakura",
        "Hinata", "Naruto", "Ronaldo", "Saske",
        "Gojo", "Messi",
    ]

    STRATEGIES = [AggressiveStrategy, CautiousStrategy, AnalystStrategy]

    def create_ai_player(self):
        name = random.choice(self.NAMES)
        self.NAMES.remove(name)

        strategy_class = random.choice(self.STRATEGIES)
        strategy = strategy_class()

        return AIPlayer(name, strategy)

    def create_ai_players(self, count):
        players = []
        for _ in range(count):
            players.append(self.create_ai_player())
        return players