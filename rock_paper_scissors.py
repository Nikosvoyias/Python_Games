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
    player_input = input("Choose: ")
    while player_input not in ["rock", "paper", "scissors"]:
        print("Wrong input. Choose again")
        player_input = input("Choose: ")

    computer_random = randrange(3)
    if computer_random == 0:
        computer_choice = "rock"
    elif computer_random == 1:
        computer_choice = "scissors"
    else:
        computer_choice = "paper"

    if player_input == "rock":
        if computer_choice == "rock":
            winner = "draw"
        elif computer_choice == "paper":
            winner = "computer"
        else:
            winner = "player"
    elif player_input == "paper":
        if computer_choice == "rock":
            winner = "player"
        elif computer_choice == "paper":
            winner = "draw"
        else:
            winner = "computer"
    else:
        if computer_choice == "rock":
            winner = "computer"
        elif computer_choice == "paper":
            winner = "player"
        else:
            winner = "draw"

    if winner == "player":
        score[0] += 1
    elif winner == "computer":
        score[1] += 1

    history.append("Round " + str(round_number) + ": Player: "
                   + player_input + ", Computer: "
                   + computer_choice + ", Score: " + str(score[0]) + "-" + str(score[1]))
    print("Computer pick: " + computer_choice)
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
