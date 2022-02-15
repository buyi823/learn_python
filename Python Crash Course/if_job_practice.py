#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-08-30 11:14
# if practice

alien_color = 'red'

if alien_color == 'green':
    print("Your got five points!")
elif alien_color == 'yellow':
    print("Your got ten points!")
elif alien_color == 'red':
    print("Your got fiften points")

age = 36

if age < 2:
    print('baby')
elif age >= 2 and age < 4:
    print('infant')
elif age >= 4 and age < 13:
    print('child')
elif age >= 13 and age < 20:
    print('teenager')
elif age >= 20 and age < 65:
    print('adult')
elif age >= 65:
    print('elder')

favorite_fruits = ['apple', 'bananas', 'peach']
if 'apple' in favorite_fruits:
    print('You really like apple!')
if 'bananas' in favorite_fruits:
    print('You really like bananas')
if 'peach' in favorite_fruits:
    print('You really like peach')