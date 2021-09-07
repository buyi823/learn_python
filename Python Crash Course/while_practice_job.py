#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-07 14:33
# while job practice

flag = True
places = {}

while flag:
    print("\nIf you could visit one placce in the world, where ould you go? ")
    name_place = input("Please input place: ")
    places[name_place] = name_place 
    
    repeat = input("And others places? yes/no? ")
    if repeat == 'no':
        flag = False

print("You choice's places: ")
print(places)