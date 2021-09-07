#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-03-15:14:41
# input jobe practice

car = input("What kind can you want rent?")

print(f"Let me see if I can find you a {car}")

order = input("How many of you have dinner?")
order = int(order)

if order <= 8:
    print("ok")
else:
    print("Sorry we have no enough table.")