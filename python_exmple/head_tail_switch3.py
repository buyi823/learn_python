#!/usr/bin/python3
# 将列表中的头尾两个元素对调


def swapList(list):
    get = list[-1], list[0]
    list[0], list[-1] = get
    return list


newList = [1, 2, 3]
print(swapList(newList))