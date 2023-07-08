# рука из пяти карт, только номиналы, J=11, Q=12, K=13, A=1
# найти самую старшую комбинацию в руке
    # старшая карта
    # пара
    # две пары
    # сет
    # стрит
    # фулл-хаус
    # каре

from random import randrange as rr

hand = tuple(rr(1, 14) for _ in range(5))
unique = set(hand)

# находим стрит или старшую карту
if len(unique) == 5:
    hand_sorted = sorted(hand)
    lowest_card = hand_sorted[0]
    if hand_sorted == list(range(lowest_card, lowest_card+5)):
        result = 'стрит'
    else:
        result = 'старшая карта'

# находим пару
if len(unique) == 4:
    result = 'пара'

repeated_cards = max(
    hand.count(card)
    for card in unique
)

# находим сет или две пары
if len(unique) == 3:
    if repeated_cards == 3:
        result = 'сет'
    else:
        result = 'две пары'

# находим каре или фулл-хаус
if len(unique) == 2:
    if repeated_cards == 4:
        result = 'каре'
    else:
        result = 'фулл-хаус'

print(hand)
print(result)
