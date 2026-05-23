# from model.card import Deck, CardType
# from model.player import AIPlayer
# from model.strategy import AggressiveStrategy
#
# deck = Deck()
# deck.shuffle()
#
# bot = AIPlayer("Bot1", AggressiveStrategy())
# bot.hand = deck.deal(5)
#
# print(f"{bot.name}, рука: {bot.hand}")
#
# cards, count = bot.select_cards(CardType.QUEEN, None)
# print(f"Кладе: {cards} (заявляє {count} Queen)")
#
# call = bot.decide_liar(2, CardType.QUEEN, None)
# print(f"Викликає Liar: {call}")

from player_factory import PlayerFactory

factory = PlayerFactory()
bots = factory.create_ai_players(3)

for bot in bots:
    print(f"{bot.name} — стратегія: {bot.strategy.__class__.__name__}")