from model.card import CardType
from model.player import AIPlayer
from model.strategy import AggressiveStrategy, CautiousStrategy
from model.game import Game

bot1 = AIPlayer("Gojo", AggressiveStrategy())
bot2 = AIPlayer("Ronaldo", CautiousStrategy())

game = Game([bot1, bot2])
game.start_new_round()

r = game.current_round
print(f"Карта раунду: {r.round_card.value}")
print(f"Рука {bot1.name}: {bot1.hand}")
print(f"Рука {bot2.name}: {bot2.hand}")

cards, count = bot1.select_cards(r.round_card, None)
print(f"\n{bot1.name} кладе {cards}")
bot1.remove_cards(cards)
r.play_cards(cards)

# Бот2 вирішує чи кликати Liar
is_liar_call = bot2.decide_liar(count, r.round_card, None)
print(f"{bot2.name} кличе Liar: {is_liar_call}")

if is_liar_call:
    was_lying = r.check_liar(cards)
    if was_lying:
        print(f"{bot1.name} брехав! Крутить револьвер...")
        game.pull_trigger(bot1)
    else:
        print(f"{bot1.name} був чесний! {bot2.name} крутить револьвер...")
        game.pull_trigger(bot2)

print(f"\n{bot1.name} живий: {bot1.is_alive}")
print(f"{bot2.name} живий: {bot2.is_alive}")