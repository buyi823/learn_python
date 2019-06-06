#!usb/bin/python3
# -*- coding: UTF-8 -*-
# Filename : variable switch
# author by : Blainexu

x = input('输入 x 值: ')
y = input('输入 y 值: ')

# 创建临时变量，并交换
# temp = x
# x = y
# y = temp

# 不适用临时变量
x,y = y,x

print('交换后x的值为：{}'.format(x))
print('交换后y的值为：{}'.format(y))

