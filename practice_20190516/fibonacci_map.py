#!/usr/bin/python3
#使用Lambda和map函数生成斐波那契数列

n = int(input('Enter the number of terms: '))

def fibonacci(count):
    fib_list = [0,1]
    any(map(lambda _: fib_list.append(sum(fib_list[-2:])),range(2,count)))
    return fib_list[:count]

print(fibonacci(n))