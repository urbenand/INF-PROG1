#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created on Sat Sep 30 16:47:21 2023

# @author: Andreas Urben

# Ask for systolic value
systolic = int(input("Please enter systolic blood pressure value:"))
# Ask for diastolic value
diastolic = int(input("Please enter diastolic blood pressure value:"))

patient_status = "Undefined"

# normal
if systolic < 120 and diastolic < 80:
    patient_status = "has normal blood pressure."

# elevated
elif 120 <= systolic <= 129 and diastolic < 80:
    patient_status = "has elevated blood pressure."
    
# hypertension st 1
elif 130 <= systolic <= 139 or 80 <= diastolic <= 89:
    patient_status = "is in Hypertension Stage 1."

# hypertension st 2
elif systolic >= 140 or diastolic >= 90:
    patient_status = "is in Hypertension Stage 2."

# hypertensive crisis
elif systolic > 180 or diastolic > 120:
    patient_status = "is in a hypertensive crisis. Seek immediate medical attention."

# print result to console
print(f"The patient {patient_status}")
