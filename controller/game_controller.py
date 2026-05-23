from model.game import Game
from model.player import HumanPlayer
from model.round import Round
from player_factory import PlayerFactory
from view.console_view import ConsoleView


class GameController:

    def __init__(self):
        self.view = ConsoleView()
        self.game = None

    def setup(self):
        factory = PlayerFactory()
        human = HumanPlayer(input("Введи своє ім'я: "))
        bots = factory.create_ai_players(3)

        players = [human] + bots
        self.game = Game(players)
        self.game.add_observer(self.view)

    def run(self):
        self.setup()

        while not self.game.is_game_over():
            self.play_round()

        winner = self.game.get_winner()
        self.game.notify("game_over", {"winner": winner})

    def play_round(self):
        input("\nНатисни Enter щоб почати раунд...")
        self.game.start_new_round()
        r = self.game.current_round

        last_cards = None
        last_player = None

        while True:
            current = r.get_current_player()

            if not current.is_alive:
                r.advance_turn()
                continue

            if last_cards is not None:
                liar_caller = self._check_all_for_liar(
                    current, last_player, last_cards, r
                )

                if liar_caller is not None:
                    self.resolve_liar(last_player, liar_caller, last_cards, r)
                    return

            if len(current.hand) == 0:
                r.advance_turn()
                continue

            cards, claimed_count = current.take_turn(r.round_card, self.view)
            current.remove_cards(cards)
            r.play_cards(cards)

            self.game.notify("cards_played", {
                "player": current,
                "claimed_count": claimed_count,
                "round_card": r.round_card
            })

            last_cards = cards
            last_player = current
            r.advance_turn()

    def _check_all_for_liar(self, current, last_player, last_cards, r):
        alive = [p for p in r.players if p.is_alive and p != last_player]

        for player in alive:
            is_call = player.decide_liar(
                len(last_cards), r.round_card, self.view
            )
            if is_call:
                return player
            else:
                self.view.show_pass(player)

        return None

    def resolve_liar(self, target, caller, cards, r):
        self.game.notify("liar_called", {
            "caller": caller,
            "target": target
        })

        was_lying = r.check_liar(cards)

        self.game.notify("liar_result", {
            "was_lying": was_lying,
            "target": target,
            "caller": caller
        })

        if was_lying:
            shooter = target
        else:
            shooter = caller

        self.game.pull_trigger(shooter)
        input("\nНатисни Enter щоб продовжити...")