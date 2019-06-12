#!/usr/bin/python3
# 计算元素在列表中出现的次数


def countX(lst, x):
    return lst.count(x)


lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# print(lst.count(10))
x = 8
print(countX(lst, x))
