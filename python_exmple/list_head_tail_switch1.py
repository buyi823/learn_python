#!/usr/bin/python3

# 将列表中的头尾两个元素对调


def swapList(newList):
    size = len(newList)

    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList


newList = [1, 2, 3]

print(swapList(newList))