from model.round import Round
from model.revolver import Revolver

class Game:

    def __init__(self, players):
        self.players = players
        self.revolvers = {}
        for player in players:
            self.revolvers[player.name] = Revolver()
        self.observers = []
        self.current_round = None

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, event, data):
        for observer in self.observers:
            observer.update(event, data)

    def get_alive_players(self):
        return [p for p in self.players if p.is_alive]

    def is_game_over(self):
        alive = self.get_alive_players()
        return len(alive) <= 1

    def get_winner(self):
        alive = self.get_alive_players()
        if len(alive) == 1:
            return alive[0]
        return None

    def start_new_round(self):
        self.current_round = Round(self.players)
        self.notify("new_round", {
            "round_card": self.current_round.round_card,
            "players": self.current_round.players
        })

    def pull_trigger(self, player):
        revolver = self.revolvers[player.name]
        is_shot = revolver.pull_trigger()

        if is_shot:
            player.is_alive = False
            self.notify("player_dead", {"player": player})
        else:
            self.notify("player_survived", {"player": player})

        return is_shot