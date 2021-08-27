#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-08-27 16:08
# tuple practice

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# 元组是由逗号标识的，如果元组只有一个元素那么：
# my_t = (3,)
# 遍历元组
for dimension in dimensions:
    print(dimension)
    
# 可以给元组变量重新赋值
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)
    
food = ('bread', 'milk', 'coffee', 'sandwich', 'ice cream')
print("We offer the following foods:")
for f in food:
    print(f)
