#!/usr/bin/python3
# 使用Lambda和Reduce函数生成斐波那契数列

from functools import reduce

n = int(input('Enter the number of terms: '))


def fib(n):
    return reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1])


print(fib(n))

