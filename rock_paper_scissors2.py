from random import randrange
from random import seed
from datetime import datetime

seed(datetime.now())

round_number = 0
score = [0, 0]
history = []
while True:
    round_number += 1
    print("Round: " + str(round_number))
    player_input_str = input("Choose: ")
    while player_input_str not in ["rock", "paper", "scissors"]:
        print("Wrong input. Choose again")
        player_input_str = input("Choose: ")

    if player_input_str == "rock":
        player_input_int = 0
    elif player_input_str == "scissors":
        player_input_int = 1
    else:
        player_input_int = 2

    computer_choice_int = randrange(3)
    if computer_choice_int == 0:
        computer_choice_str = "rock"
    elif computer_choice_int == 1:
        computer_choice_str = "scissors"
    else:
        computer_choice_str = "paper"

    diff = player_input_int - computer_choice_int

    if diff == -1 or diff == 2:
        winner = "player"
    elif diff == -2 or diff == 1:
        winner = "computer"
    else:
        winner = "Draw"

    if winner == "player":
        score[0] += 1
    elif winner == "computer":
        score[1] += 1

    history.append("Round " + str(round_number) + ": Player: "
                   + player_input_str + ", Computer: "
                   + computer_choice_str + ", Score: " + str(score[0]) + "-" + str(score[1]))
    print("Computer pick: " + computer_choice_str)
    print("Player - Computer: " + str(score[0]) + "-" + str(score[1]))

    if score[0] == 3:
        print("Player wins!")
        print("")
        for item in history:
            print(item)
        break
    elif score[1] == 3:
        print("Computer wins!")
        print("")
        for item in history:
            print(item)
        break

    print("======================\n")
