#!/usr/bin/python3
# 计算元素在列表中出现的次数
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

lst = [8, 6, 8, 10, 8, 20, 10, 8, 8] 
x = 8
print(countX(lst, x))