# main.py (тимчасовий тест)

from model.card import Deck

deck = Deck()
print(f"Карт в колоді: {len(deck)}")

deck.shuffle()
hand = deck.deal(5)

print(f"Роздано: {hand}")
print(f"Залишилось: {len(deck.cards)}")
