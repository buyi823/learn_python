#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-01 16:49
# 在字典中存储列表

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings: ")
for topping in pizza['toppings']:
    print("\t" + topping)
    
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are: ")
    for language in languages:
        print(f"\t{language.title()}")