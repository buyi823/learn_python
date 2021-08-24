#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine
# Time: 2021-07-06 22:29:08
# Description: List practice

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

nba_super_star = ["Michael Jordan", 'Kobe Bryant', "Allen Iverson", 'Vincent Carter']
print(nba_super_star)

for super_star in nba_super_star:
    message = f"Hello, {super_star}!"
    print(message)

triffic = ['walk', 'run', 'bicycle', 'bus', 'taxi', 'motorcycle', 'car']
my_way = f"I would like to own a {triffic[6].title()}"
print(my_way)
