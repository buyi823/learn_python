#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-08-27 17:17
# if pracitce   conditional test

a = 'abc'
b = 'Abc'
if a == b:
    print('true')
else:
    print(a, b)

if a != b:
    b = b.lower()
    if a == b:
        print('True')
    else:
        print(a, b)

john_age = 21
marry_age = 18
john_gender = 'male'
marry_gender = 'female'
if john_age >= 20:
    print('you can drink some wine')
if marry_age >= 18 and marry_gender == 'female':
    print('you can marry')

cars = ['audi', 'ferrari', 'bens', 
        'Rolls-Royce', 'honda', 'Lamborghini', 'Porsche']

my_favorite_car = 'buick'
if my_favorite_car in cars:
    print(f"Your favorite car is:{my_favorite_car}")
else:
    print("Sorry, we don't have your favorite car.")
    
age = 12
if age < 4:
    print('your admission cost is 0')
elif age < 18:
    print('your admission cost is $25')
else:
    print('your admission cost is %40.')
    
# 为了让代码更简洁可以写成下面的：
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admassion cost is ${price}.")