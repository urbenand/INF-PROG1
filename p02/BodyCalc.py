#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created on Sat Sep 30 13:23:47 2023
# @author: Andreas Urben

import math


def set_data():
    # Ask user for weight
    user_weight = int(input("Insert your weight (in Kg): "))
    # Ask user for height
    user_height = int(input("Insert your height (in cm): "))

    # write information into list "data"
    data = [user_weight, user_height]

    # return data
    return data


def get_bsa(data, formatted=False):
    weight = data[0]
    height = data[1]

    bsa = math.sqrt(height * weight / 3600)

    if formatted:
        bsa = format(bsa, '.2f')

    # return calculated BSA
    return bsa


def get_bmi(data, formatted=False):
    # get information from data list
    weight = data[0]
    height = data[1]

    # calculate BMI by using params
    bmi = weight / (height / 100) ** 2

    # if formatted, then return as string
    if formatted:
        bmi = format(bmi, '.2f')

    # return calculated BMI
    return bmi
