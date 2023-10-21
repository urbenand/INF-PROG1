#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created on Sat Sep 30 12:21:34 2023
# @author: Andreas Urben

# import BMI Class
import BodyCalc

# ask for data
data = BodyCalc.set_data()

# get BMI, second param defines wether it's formatted or not
bmi = BodyCalc.get_bmi(data, True)

# get BSA, second param defines wether it's formatted or not
bsa = BodyCalc.get_bsa(data, True)

# output BMI and BSA
print("Your Body Mass Index (BMI) is: ", bmi)
print("Your Body Surface Area is: ", bsa, "m^2")
