#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-03-14:52:01
# input and while practice

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# prompt = "If you tell us who you are, we can personalize the message you see."
# prompt += "\nWhat is your first name?"
# name = input(prompt)
# print(f"\nHello, {name}!")

# age = input("How old are you? ")
# age = int(age)
# print(age >= 18)

number = input("Please intpu a number: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
