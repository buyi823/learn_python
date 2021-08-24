#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-08-23 15:31
#  digits

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(digits))
print(min(digits))
print(sum(digits))

# list comprehension 列表解析
squres = [value**2 for value in range(1, 11)]
print(squres)

# 使用for循環打印1-20
print(value for value in range(1, 21))

# 打印一句话的第一个字符
text = "my house is full of flowers"
first_character = []
for word in text.split():
    first_character.append(word[0])
print(first_character)

first_char = [word[0] for word in text.split()]
