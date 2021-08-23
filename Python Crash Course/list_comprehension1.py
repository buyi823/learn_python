#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-08-23 19:12
# list comprehension

numbers = [number for number in range(1, 10001)]
print(numbers)

list_numbers = [number for number in range(1, 1000000)]
print(sum(list_numbers))

# 1-20的奇数
odd_number = [number for number in range(1, 20) if number % 2 != 0]
print(odd_number)

# 31以内能被3整除的数
div_numbers = [number for number in range(3, 31) if number % 3 == 0]
print(div_numbers)

# 11以内的整数的立方
cub_numbers = [number**3 for number in range(1, 11)]
print(cub_numbers)

# 21以内偶数的立方
even_numbers = [number**3 for number in range(1, 21) if number % 2 == 0]
print(even_numbers)
