#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine
# Time: 2021-07-09 20:09:42
# Description: list operation jobs

place = ['toyko', 'london', 'paris', 'new york', 'los angeles', 'las vegas', 'san francisco']
print(f'I want to go {place}')
print(f'I want to go {sorted(place)}')
print(f'I want to go {place}')
place.reverse()
print(f'I want to go {place}')
place.reverse()
print(f'I want to go {place}')
place.sort()
print(f'I want to go {place}')
place.sort(reverse=True)
print(f'I want to go {place}')
print(f'Total city: {len(place)}')
