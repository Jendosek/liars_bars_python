from model.player import AIPlayer
from model.strategy import AggressiveStrategy, CautiousStrategy
from model.game import Game
from view.console_view import ConsoleView

bot1 = AIPlayer("Gojo", AggressiveStrategy())
bot2 = AIPlayer("Levi", CautiousStrategy())

game = Game([bot1, bot2])

view = ConsoleView()
game.add_observer(view)

game.start_new_round()

r = game.current_round
cards, count = bot1.select_cards(r.round_card, None)
bot1.remove_cards(cards)
r.play_cards(cards)

game.notify("cards_played", {
    "player": bot1,
    "claimed_count": count,
    "round_card": r.round_card
})

game.pull_trigger(bot2)