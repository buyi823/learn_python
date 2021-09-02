#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-02 17:36
# dictionary jobe practice

favorite_places = {
    'blaine': {
        'place_1': 'new york',
        'place_2': 'london',
        'place_3': 'paris',
        'place_4': 'toyko',
    },
    'no_name': {
        'place_1': 'Afghanistan',
        'place_2': 'iraq',
        'place_3': 'iran',
        'place_4': 'north korea',
    },
    'someone': {
        'place_1': 'beijing',
        'place_2': 'shanghai',
        'place_3': 'guangzhou',
        'place_4': 'shenzhen',
    },
    
}

for name, place in favorite_places.items():
    print(f"My name is {name.title()} and my favorite places below this:")
    places = f"{place['place_1']}, {place['place_2']}, {place['place_3']}, {place['place_4']}"
    print(f"{places}\n")