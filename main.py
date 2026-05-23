from model.card import Deck, CardType
from model.strategy import AggressiveStrategy, CautiousStrategy, AnalystStrategy

deck = Deck()
deck.shuffle()
hand = deck.deal(5)

print(f"Рука: {hand}")
print(f"Карта раунду: Queen")
print()

for name, strategy in [("Агресор", AggressiveStrategy()),
                        ("Обережний", CautiousStrategy()),
                        ("Аналітик", AnalystStrategy())]:
    cards, count = strategy.choose_cards(hand, CardType.QUEEN)
    call = strategy.should_call_liar(2, CardType.QUEEN, hand)
    print(f"{name}: кладе {cards}, викликає Liar: {call}")