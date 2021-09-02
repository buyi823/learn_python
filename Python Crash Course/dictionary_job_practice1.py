#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-08-31 17:12
# dictionary job practice

terms = {
    'term1': 'inherit',
    'term2': 'oop',
    'term3': 'polymorphism',
    'term4': 'whatever',
    'term5': 'ops'
}
for k, v in terms.items():
    print(f"{k}: {v}")
    
rivers = {
    'nile': 'egypt',
    'Mississippi': 'usa',
    'amazon': 'brazil',
    'yellow river': 'china',
    'rhine': 'germany'
}
for k, v in rivers.items():
    print(f"\nThe {k.title()} runs through {v.title()}")
    
users = {'john': 'c', 'anna': 'java', 'blaine': 'python', 'michael': 'c++'}
name = ['john', 'michael']

for k in users.keys():
        print(f"Hi {k.title()}.")
        if k in name:
            names = k.title()
            print(f"Thank you: {names}")


