#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created on Sat Sep 30 17:05:45 2023

# @author: Andreas Urben

# SINGLE ROUND ROCK PAPER SCISSORS

# import random
import random


# convert user input values
def for_machine(val):
    res = 0
    if val == "Pill":
        res = 1
    elif val == "Scalpel":
        res = 2
    elif val == "Prescription":
        res = 3
    return int(res)


# convert machine values
def readable(val):
    res = 0
    if val == 1:
        res = "Pill"
    elif val == 2:
        res = "Scalpel"
    elif val == 3:
        res = "Prescription"
    return res


print("Welcome to the Medical Rock, Paper, Scissors Game!")
print("Rules: Pill crushes Scalpel, Scalpel cuts Prescription, Prescription covers Pill.")

user_input = input("Choose Pill, Scalpel or Prescription: ")

# Print empty line
print()

computer_input = random.randint(1, 3)
user_input = for_machine(user_input)

print(f"Computer chose {readable(computer_input)}")

winner = "Undefined"

if computer_input == user_input:
    winner = "We have a tie!"

# Case where player wins
elif computer_input == 1 and user_input == 3:
    winner = "You win!"
elif computer_input == 2 and user_input == 1:
    winner = "You win!"
elif computer_input == 3 and user_input == 2:
    winner = "You win!"

# Cases where Computer wins
elif computer_input == 1 and user_input == 2:
    winner = "Computer wins!"

elif computer_input == 2 and user_input == 3:
    winner = "Computer wins!"

elif computer_input == 3 and user_input == 1:
    winner = "Computer wins!"

print(winner)
