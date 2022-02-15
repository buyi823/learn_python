#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-03-17:56:18
# while job practice

while True:
    age = input("Please input you age: ")
    print(age)
    age = int(age)
    if age < 3:
        print("Free")
        break
    elif age > 3 and age < 12:
        print("$10")
        break;
    elif age > 12:
        print("$15")
        break