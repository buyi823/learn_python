#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-08-30 18:01
# dictionary practic

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# 添加字典的键值
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)