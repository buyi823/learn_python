#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine
# Time: 2021-07-09 19:54:50
# Description: list sort

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# 对于列表的排序是永久性的
cars.sort(reverse=True)
print(cars)

# sorted()临时排序
cars1 = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list: ")
print(cars1)
print("Here is the sorted list: ")
print(sorted(cars1))
print("Here is the original list: ")
print(cars1)

cars1.reverse() # 反转列表元素的排列顺序，永久改变的，不过再执行一次就回来了
print(cars1)