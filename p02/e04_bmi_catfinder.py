#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created on Sat Sep 30 16:06:01 2023
# @author: Andreas Urben

# import BMI class
import BodyCalc

# ask for data
data = BodyCalc.set_data()

# get BMI
bmi = BodyCalc.get_bmi(data, False)

# set default value undefined
bmi_cat = "Undefined"

# define values by using calculated BMI
if bmi < 18.5:
    bmi_cat = "is underweight"
elif bmi < 25:
    bmi_cat = "has a normal weight"
elif bmi < 30:
    bmi_cat = "is overweight"
elif bmi >= 30:
    bmi_cat = "has obesity"

# print result
print("The patient", bmi_cat)
