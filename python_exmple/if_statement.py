#!usb/bin/python3
# -*- coding: UTF-8 -*-
# Filename : if
# author by : Blainexu

# user input number
num = float(input('Please input a number: '))
if num > 0:
    print('positive number')
elif num == 0:
    print('zero')
else:
    print('negative')