#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-02 17:01
# dictionary practice

users = {
    'jordan': {
        'first': 'michael',
        'last': 'jordan',
        'position': 'shooting guard',
    },
    'kobe': {
        'first': 'kobe',
        'last': 'bryant',
        'position': 'shooting guard',
    },
    'james': {
        'first': 'lebron',
        'last': 'james',
        'position': 'small forward',
    },
}
print(users)
for player, player_info in users.items():
    print(f"\nPlayer: {player}")
    full_name = f"{player_info['first']} {player_info['last']}"
    position = player_info['position']
    
    print(f"\tPlayer full name: {full_name.title()}")
    print(f"\tPosition: {position.title()}")