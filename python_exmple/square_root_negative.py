# -*- coding: UTF-8 -*-
#!/usr/bin/python3

# Filenname: squart root negative.py
# author by : Blaine Xu
import cmath

num = float(input('please input a number: '))
num_sqrt = cmath.sqrt(num)
print('{0}的平方根为{1:0.3f}+{2:0.3f}j'.format(num,num_sqrt.real,num_sqrt.imag))