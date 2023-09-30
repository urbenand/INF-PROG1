#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#Created on Sat Sep 30 16:06:01 2023
#@author: andreasurben

# import BMI class
import BodyCalc

# ask for data
data = BodyCalc.helper.setData()

# get BMI
bmi = BodyCalc.helper.getBMI(data, False)

# set default value undefined
bmiCat = "Undefined"

# define values by using calculated BMI
if bmi < 18.5:
    bmiCat = "is underweight"
elif bmi < 25:
    bmiCat = "has a normal weight"
elif bmi < 30:
    bmiCat = "is overweight"
elif bmi >= 30:
    bmiCat = "has obesity"

# print result
print("The patient",bmiCat)