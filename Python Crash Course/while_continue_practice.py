#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-03-17:46:28
# while continue

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


while True:
    pizza = input("Please input some Ingredients： ")
    if pizza == 'quit':
        break
    else:
        print(f"Your pizza ingredient is {pizza}")