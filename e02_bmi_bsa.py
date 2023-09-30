#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#Created on Sat Sep 30 12:21:34 2023
#@author: andreasurben

# import math library
import math

# import BMI Class
import BMI

# Ask user for weight
userWeight = int(input("Insert your weight (in Kg): "))

# Ask user for height
userHeight = int(input("Insert your height (in cm): "))

# Calculate BSA
# Option 1
    # bsa = math.sqrt(userHeight * userWeight / 3600)
    
    # Round BSA to 2 digits
    #bsa = round(bsa, 2)

# Option 2
# direct method
bsa = format(math.sqrt(userHeight*userWeight/3600),'.2f')

# Calculate BMI, Option 1
bmi = format(userWeight / (userHeight/100)**2,'.2f')

# output BMI and BSA
print("Your Body Mass Index (BMI) is: ",bmi)
print("Your Body Surface Area is: ",bsa,"m^2")