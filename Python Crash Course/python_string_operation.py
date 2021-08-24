#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 字符串操作


name = 'aDa lovelace'
# title()将单词首字母改为大写,其他小寫
print(name.title())
# upper()將所有字母改爲大寫
print(name.upper())
# lower()將所有字母改爲小寫
print(name.lower())

# 在字符串中使用变量
first_name = 'ada'
last_name = 'lovelace'
# f是format的缩写，可以将变量放在花括号内（3.6引入的）
full_name = f"{first_name} {last_name}"
print(full_name)
message = f'Hello, {full_name.title()}!'
print(message)
# 如果是3.6之前的版本可以使用format()
# full_name = "{} {}".format(first_name, last_name)

print("\n")
# 使用制表符或者换行符来添加空白
print('Languages:\n\tPython\n\tC\n\tJavaScript')

# 删除空白
favorite_language = 'Python '
# rstrip()删除空白，不过下面这一条语句删除空白并未改变变量
print(favorite_language.rstrip())
# lstrip()删除头部的空白
favorite_language = ' Python'
print(favorite_language)
print(favorite_language.lstrip())
# strip()删除两端的空白
favorite_language = '  Python  '
print(len(favorite_language))# 输出字符串长度
print(favorite_language.strip())# 输出去掉空格的字符串
print(len(favorite_language.strip()))

# 单引号和双引号, 撇号位于两个双引号之间，因此python解释器能够正确的理解这个字符串
message = "One of Python's strengths is its diverse community."
print(message)

