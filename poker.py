from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

kind = {"heart", "diamond", "spade", "club"}
number = {"ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"}

deck = {(k, n) for k in kind for n in number}

player1 = set()
player2 = set()

list_deck = list(deck)
for _ in range(5):
    pos1 = randrange(len(list_deck))
    player1.add(list_deck.pop(pos1))
    pos2 = randrange(len(list_deck))
    player2.add(list_deck.pop(pos2))
print(player1)
print(player2)

player1 = {('spades', "ace"), ('heart', 4), ('club', 5), ('diamond', 3), ('spades', 2)}
cnt = 0
for card in player1:
    if card[1] == "ace":
        cnt += 1
if cnt == 4:
    print("Player 1 has four of a kind!")

cnt = 0
for card in player2:
    if card[1] == "ace":
        cnt += 1
if cnt == 4:
    print("Player 2 has four of a kind!")

hand_numbers = []
for card in player1:
    if card[1] == "ace":
        hand_numbers.append(1)
    elif card[1] == "jack":
        hand_numbers.append(11)
    elif card[1] == "queen":
        hand_numbers.append(12)
    elif card[1] == "king":
        hand_numbers.append(13)
    else:
        hand_numbers.append(card[1])


hand_numbers.sort()
print(hand_numbers)

for pos in range(4):
    if hand_numbers[pos] != hand_numbers[pos+1] - 1:
        break
else:
    print("You have straight!")
