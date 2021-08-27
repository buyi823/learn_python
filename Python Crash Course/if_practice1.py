#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-08-27 16:45
# if practice

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
requested_topping = "mushrooms"
if requested_topping != 'anchovies':
    print('Hold the anchovies')
    
vegetable = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in vegetable) # in  检查列表是否包含
bannded_user = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in bannded_user:
    print(f"{user.title()}, you can post a response if you wish.")
    
car = 'subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

