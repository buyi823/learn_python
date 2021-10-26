#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine
# Time: 2021-07-08 23:29:56
# Description: List operation practice

party_guys = ['Michale', 'John', 'Chris', 'Elizabeth', 'Phoebe', 'Rachel']
# 这种输出也可以，输出带括号
print(f'I want to invite {party_guys[0], party_guys[2], party_guys[4]}')
print(f'I want to invite {party_guys[0]}, {party_guys[2]} and {party_guys[4]}')
party_guys[0] = 'Harry'
print(f'But Michale couldn\'t come, so I decided to invite {party_guys[0]},{party_guys[2]} and {party_guys[4]}')

party_guys.insert(0, 'Kobe')
party_guys.insert(7, 'James')
party_guys.append('Monica')
print(f'All the people who were invited: {party_guys}')

while len(party_guys) > 2:
    guy1 = party_guys.pop()
    print(f'I\'m so sorry {guy1}')

print(f'In the end I can only invite you two {party_guys[0]} and {party_guys[1]}.')

del party_guys[0]
del party_guys[0]
print(party_guys)