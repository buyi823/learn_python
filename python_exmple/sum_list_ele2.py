#!/usr/bin/python
# 计算列表元素之和
# 使用 while() 循环
total = 0
ele = 0

list1 = [11, 5, 17, 18, 23]

while (ele < len(list1)):
    total = total + list1[ele]
    ele += 1

print("列表元素之和为: ", total)