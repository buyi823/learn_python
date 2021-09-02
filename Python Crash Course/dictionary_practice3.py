#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-08-31 15:57
# dictionary practice

user = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user.items():
    print(f"Key: {key}")
    print(f"Value: {value}")
    
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

for language in favorite_languages.values():
    print(language.title())
print('\n')
# set() 去除重复的元素
for language in set(favorite_languages.values()):
     print(language.title())