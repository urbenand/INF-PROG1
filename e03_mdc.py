#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#Created on Sat Sep 30 12:34:57 2023
#@author: andreasurben

# Ask for weight
weight = int(input("Enter your weight in kilograms: "))

# Ask for medicinal dosage
dosage = int(input("Enter the medicines dosage in mg/kg of weight: "))

# Define default capsule size in mg
capsuleSize = 100

# Define totalDosage (e.g. person is 70kg, dosage is equal to dosage * weight)
totalDosage = float(weight * dosage)

# Define requiredCapsules
requiredCapsules = int(totalDosage / capsuleSize)

# Define deficit
deficit = float(totalDosage - (requiredCapsules * capsuleSize))

# Output values
print("The total dosage of the medicine the patient should take is:", totalDosage,"mg") #4750.0 mg
print("The number of complete capsules of medicine required is:", requiredCapsules, "Capsules") # 47.0
print("The deficit in the prescribed medicine is: ", deficit,"mg") # 50.0 mg