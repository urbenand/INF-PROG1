#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created on Sat Sep 30 12:04:11 2023
# @author: Andreas Urben

# Define actual year by importing datetime and reading out today's year
import datetime

# Define Milestone Age
milestone_age = 100

# Option 1, with multiple variables
# today = datetime.date.today()
# this_year = int(today.year)

# Option 2, direct
this_year = int(datetime.date.today().year)

# Create input for current age
current_age = int(input("Aktuelles Alter/current age: "))

# Calculate year of birth
birth_year = this_year - current_age

# Calculate year, in which user turns defined milestone age
calculated_year = birth_year + milestone_age

# print german text
print(f"Sie werden im Jahre {calculated_year} das Alter von {milestone_age} erreichen")
print(f"(Geboren worden sind Sie im Jahre {birth_year}")

# print empty line
print()

# print english text
print("You will turn", milestone_age, "years old in the year:", calculated_year, ", you were born in:", birth_year)
