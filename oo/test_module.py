#!/usr/bin/python3


def average(values):
    """Computers the arithmetic mean of a list of numbers.
    >>> print(average([20,30,70]))
    40.0
    """
    return sum(values) / len(values)


import doctest
doctest.testmod()  # 自动验证嵌入测试
