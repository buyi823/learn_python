#!/usr/bin/python
# 计算列表元素之和
# 使用递归

list1 = [11, 5, 17, 18, 23]


def sumOfList(list, size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)


total = sumOfList(list1, len(list1))
print("列表元素之和为: ", total)