#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created on Sat Sep 30 17:05:45 2023

# @author: Andreas Urben

# SINGLE ROUND ROCK PAPER SCISSORS

# import random
import random


# convert user input values
def formachine(val):
    res = 0
    if val == "Pill":
        res = 1
    if val == "Scalpel":
        res = 2
    if val == "Prescription":
        res = 3
    return int(res)


# convert machine values
def readable(val):
    res = 0
    if val == 1:
        res = "Pill"
    if val == 2:
        res = "Scalpel"
    if val == 3:
        res = "Prescription"
    return res


# Win-Count User
win_user = 0
# Win Count computer
win_computer = 0
# define Round Number
roundNo = 1
# define max rounds
max_round = int(input("Enter the amount of needed wins: "))

print("Welcome to the three round Medical Rock, Paper, Scissors Game!")
print("Rules: Pill crushes Scalpel, Scalpel cuts Prescription, Prescription covers Pill.")

while win_user < max_round and win_computer < max_round:
    print()
    print("Round", roundNo)
    if roundNo > 1:
        print("Scoreboard:   User: ", win_user, "/ Computer: ", win_computer)
        print()

    user_input = input("Choose Pill, Scalpel or Prescription: ")
    # Print empty line
    print()

    computer = random.randint(1, 3)
    user_input = formachine(user_input)

    print("Computer chose", readable(computer))
    winner = "Undefined"

    # Check who wins each round
    if computer == user_input:
        winner = "We have a tie!"

    elif computer == 1 and user_input == 3:
        win_user += 1
        winner = "You win!"

    elif computer == 2 and user_input == 1:
        win_user += 1
        winner = "You win!"

    elif computer == 3 and user_input == 2:
        win_user += 1
        winner = "You win!"

    elif computer == 1 and user_input == 2:
        win_computer += 1
        winner = "Computer wins!"

    elif computer == 2 and user_input == 3:
        win_computer += 1
        winner = "Computer wins!"

    elif computer == 3 and user_input == 1:
        win_computer += 1
        winner = "Computer wins!"

    roundNo += 1
    print(winner)

else:
    print("Game over!   User: ", win_user, "/ Computer: ", win_computer)
    if win_user > win_computer:
        print("You win this game!")
    else:
        print("Computer wins this game!")
