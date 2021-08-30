#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-08-30 16:31
# check users name

current_users = ['John', 'Michael', 'James', 'Blaine', 'Chris']
new_users = ['Jordan', 'Kobe', 'michael', 'BLAINE', 'rose']

for new_user in new_users:
    if new_user.title() or new_user in current_users:
        print(f" \"{new_user}\" This user name is taken.")
    else:
        print(f" \"{new_user}\" You can use this username.")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
