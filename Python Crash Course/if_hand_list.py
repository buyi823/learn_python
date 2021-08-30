#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-08-30 11:36
# 使用if语句处理列表

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}")
print("Finished making your pizza!")

# 确保列表是否空
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print('Finished making your pizza')
else:
    print('Are you sure you want a plain pizza?')
    
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping},")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")