#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#Created on Sat Sep 30 17:05:45 2023

#@author: andreasurben

# SINGLE ROUND ROCK PAPER SCISSORS

# import random
import random

# convert user input values
def formachine(val):
    res = 0
    if userInput == "Pill":
        res = 1
    if userInput == "Scalpel":
        res = 2
    if userInput == "Prescription":
        res = 3
    return int(res)
        
# convert machine values
def readable(val):
    res = 0
    if computer == 1:
        res = "Pill"
    if computer == 2:
        res = "Scalpel"
    if computer == 3:
        res = "Prescription"
    return res

# Win-Count User
winUser = 0
# Win Count computer
winComputer = 0
# define Round Number
roundNo = 1

print("Welcome to the three round Medical Rock, Paper, Scissors Game!")
print("Rules: Pill crushes Scalpel, Scalpel cuts Prescription, Prescription covers Pill.")

while winUser < 3 and winComputer < 3:
    print()
    print("Round",roundNo)
    if roundNo > 1:
        print("Scoreboard:   User: ", winUser, "/ Computer: ", winComputer)
        print()
        
    userInput = input("Choose Pill, Scalpel or Prescription: ")
    # Print empty line
    print()
    
    computer = random.randint(1,3)
    userInput = formachine(userInput)
        
    print("Computer chose", readable(computer))
    winner = "Undefined"
    
    # Check who wins each round
    if computer == userInput:
        winner = "We have a tie!"
        
    if computer == 1 and userInput == 3:
        winUser+=1
        winner = "You win!"
        
    if computer == 2 and userInput == 1:
        winUser+=1
        winner = "You win!"
    
    if computer == 3 and userInput == 2:
        winUser+=1
        winner = "You win!"
    
    if computer == 1 and userInput == 2:
        winComputer+=1
        winner = "Computer wins!"
        
    if computer == 2 and userInput == 3:
        winComputer+=1
        winner = "Computer wins!"
        
    if computer == 3 and userInput == 1:
        winComputer+=1
        winner = "Computer wins!"
        
    roundNo+=1
    print(winner)
    
else:
    print("Game over!   User: ", winUser, "/ Computer: ", winComputer)
    if winUser > winComputer:
        print("You win this game!")
    if winComputer > winUser:
        print("Computer wins this game!")