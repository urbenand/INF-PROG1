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

print("Welcome to the Medical Rock, Paper, Scissors Game!")
print("Rules: Pill crushes Scalpel, Scalpel cuts Prescription, Prescription covers Pill.")

userInput = input("Choose Pill, Scalpel or Prescription: ")

# Print empty line
print()

computer = random.randint(1,3)
userInput = formachine(userInput)
    
print("Computer chose", readable(computer))

if computer == userInput:
    winner = "We have a tie!"

if computer == 1 and userInput == 3:
    winner = "You win!"
    
if computer == 2 and userInput == 1:
    winner = "You win!"

if computer == 3 and userInput == 2:
    winner = "You win!"

if computer == 1 and userInput == 2:
    winner = "Computer wins!"
    
if computer == 2 and userInput == 3:
    winner = "Computer wins!"
    
if computer == 3 and userInput == 1:
    winner = "Computer wins!"
    
print(winner)