#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine
# Time: 2021-07-25 18:33:26
# Description: 數值列表

for value in range(1, 5):
    print(value)

# 使用range()創建列表
numbers = list(range(1, 6))
print(numbers)

# range() 可以指定步長。例如：下面打印1-10的偶数
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# ** 乘方运算
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"min: {min(digits)}")
print(f"max: {max(digits)}")
print(f"sum: {sum(digits)}")