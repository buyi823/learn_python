#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-08-24-11:21:35
# slice 

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
# 遍历切片
print("Here are the first three playerson my team:")
for player in players[:3]:
    print(player.title())

# 复制列表
my_foods = ['pizza','falafel', 'carrot cake']
friend_foods = my_foods[:]
print(f"my favorite foods are: {my_foods}")
print(f"My friend's favorite foodsare:{friend_foods}")
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(f"my favorite foods are: {my_foods}")
print(f"My friend's favorite foodsare:{friend_foods}")
# friend_foods =my_foods这是将两个变量指向同一个列表了， 使用切片[:]是将一个副本赋给新的

