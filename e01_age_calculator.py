#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#Created on Sat Sep 30 12:04:11 2023
#@author: andreasurben

# Define Milestone Age
milestoneAge = 100

# Define acutal year by importing datetime and reading out todays year
import datetime

# Option 1, with multiple variables
# today = datetime.date.today()
# thisYear = int(today.year)

# Option 2, direct
thisYear = int(datetime.date.today().year)

# Create input for current age
currentAge = int(input("Aktuelles Alter/current age: "))

# Calculate year of birth
birthYear = thisYear - currentAge

# Calculate year, in which user turns defined milestone age"
calculatedYear = birthYear + milestoneAge

# print german text
print("Sie werden im Jahre", calculatedYear, "das Alter von", milestoneAge, "erreichen. Geboren worden sind Sie im Jahre", birthYear)

# print empty line
print()

# print english text
print("You will turn", milestoneAge, "years old in the year:",calculatedYear,", you were born in:",birthYear)