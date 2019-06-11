#!/usr/bin/python3
# 将列表中的头尾两个元素对调

def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0]
    return newList

newList=[1,2,3]
print(swapList(newList))
