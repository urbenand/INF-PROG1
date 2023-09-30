#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#Created on Sat Sep 30 12:21:34 2023
#@author: andreasurben

# import math library
import math

# import BMI Class
import BodyCalc

# ask for data
data = BodyCalc.helper.setData()

# get BMI, second param defines wether it's formatted or not
bmi = BodyCalc.helper.getBMI(data, True)

# get BSA, second param defines wether it's formatted or not
bsa = BodyCalc.helper.getBSA(data, True)

# output BMI and BSA
print("Your Body Mass Index (BMI) is: ",bmi)
print("Your Body Surface Area is: ",bsa,"m^2")