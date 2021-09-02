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

# 修改字典的值
alien_0['color'] = 'yellow'
print(alien_0)

alien_0['speed'] = 'medium'
print(alien_0)

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New postion: {alien_0['x_position']}")

# del dictionary
del alien_0['points']
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
languages = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {languages}")

for name, language in favorite_languages.items():
    print(name, language)

for name in favorite_languages.keys():
    print(name)

# get()来访问
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)