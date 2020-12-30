#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
# 在数学上，费波那契数列是以递归的方法来定义：

# Method 1

def fib(n): 
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

# The 10th Fibonacci sequence is output
print("The 10th digit in the Fibonacci sequence is:", fib(10))

# Method 2
# Using a recursive
def fib1(m):
    if m==1 or m==2:
        return 1
    return fib1(m-1)+fib1(m-2)

print("The 10th digit in the Fibonacci sequence is:", fib1(10))