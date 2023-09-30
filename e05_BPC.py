#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#Created on Sat Sep 30 16:47:21 2023

#@author: andreasurben

# Ask for systolic value
systolic = int(input("Please enter systolic blood pressure value:"))
# Ask for diastolic value
diastolic = int(input("Please enter diastolic blood pressure value:"))

patientStatus = "Undefined"

# normal
if systolic < 120 and diastolic < 80:
    patientStatus = "has normal blood pressure."
    
# elevated
if systolic >= 120 and systolic <=129 and diastolic < 80:
    patientStatus = "has elevated blood pressure."
    
# hypertension st 1
if systolic >= 130 and systolic <=139 or diastolic >=80 and diastolic <=89:
    patientStatus = "is in Hypertension Stage 1."
    
# hypertension st 2
if systolic >= 140 or diastolic >= 90:
    patientStatus = "is in Hypertension Stage 2."

# hypertensive crisis
if systolic > 180 or diastolic > 120:
    patientStatus = "is in a hypertensive crisis. Seek immediate medical attention."

# print result to console
print("The patient",patientStatus)
