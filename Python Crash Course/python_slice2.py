#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-08-24-16:32:03
# slice practice
nba_stars=['kobe','james', 'paython','westbrook', 'towns', 'paul']
print(f"The first three items in the list are: {nba_stars[:3]}")
print(f"Three items from the middle of the list are: {nba_stars[1:4]}")
print(f"The last three items in the list are: {nba_stars[-3:]}")

my_pizzas = ['fruit', 'meat', 'beef']
myfriend_pizzas = my_pizzas[:]
for pizza in my_pizzas:
    print(pizza)

myfriend_pizzas.append("i don't known more pizza's name")
for pizza in myfriend_pizzas:
    print(pizza)
