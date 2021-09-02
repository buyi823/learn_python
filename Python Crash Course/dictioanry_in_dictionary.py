#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-02 15:26
# storage dictionry in dictionary

user = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princetion',
    },
    
    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
    
}
print(user)
for username, user_info in user.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name:{full_name.title()}")
    print(f"\tLocation: {location.title()}")