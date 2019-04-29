#!/usr/bin/python3

# Fibonacci series:费布拉奇数列

a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b
