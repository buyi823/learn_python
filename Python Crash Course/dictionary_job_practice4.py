#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-02 17:27
# dictionary job practcie pet list

pets = {
    'pet1': {
        'owner': 'michael',
        'type': 'dog',
    },
    'pet2': {
        'owner': 'kobe',
        'type': 'cat',
    },
    'pet3': {
        'owner': 'james',
        'type': 'hamster',
    },
}

for k, info in pets.items():
    owner = f"{info['owner']}"
    pet_type = f"{info['type']}"
    print(f"\nHi, {owner.title()}, \nYour pet is a {pet_type}")
    