#!/usr/bin/python3

# 使用递归生成斐波那契数列

n = input('Enter the number of terms: ')
def fibo(n):
    if n < 1:
        return 1
    else:
        return(fibo(n-1) + fibo(n-2))

for i in range(int(n)):
    print(fibo(i), end = ' ')