#!/usr/bin/python3
#使用for循环实现斐波那契数列

n = int(input('Enter the number of terms: '))

def Fibonacci(n):
    f0, f1 = 0, 1
    for _ in range(n):
        yield f0
        f0, f1 = f1, f0+f1

fibs = list(Fibonacci(n))
print(fibs)