#!/usr/bin/python3
# 计算 n 个自然数的立方和
def sumOfSeries(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i * i
    return sum


n = 5
print(sumOfSeries(n))