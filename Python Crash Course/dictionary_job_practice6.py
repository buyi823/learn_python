#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-02-22:40:53
# dictionary job practice

favorite_numbers = {
    'Joy': {
        'number1' : 5,
        'number2' : 8,
        'number3' : 9,
    },
    'Bill': {
        'number1' : 3,
        'number2' : 6,
        'number3' : 9,
    },
    'Lily': {
        'number1' : 1,
        'number2' : 4,
        'number3' : 7,
    },

}
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite numbers are: ")
    numbers = f"{number['number1']} {number['number2']} {number['number3']}"
    print(f"\t{numbers}\n")