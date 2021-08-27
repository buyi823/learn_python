#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-08-24 18:14
# python slice pracitce

from itertools import product
text = "My house is full of flowers"
first_charts = [word[0] for word in text.split()]
print(first_charts)

# 例3，获取两个列表对应位的乘积;
# 来个复杂的，list a=[2,3,4,5]; list b=[3,4,5,6],想要得到a，b对应位的乘积:
# number = [i*j for i,j in zip(a, b)]

# list a=['1','2','3','i','8'],现在想将a中所有能转化为数字的字符串转化为数字，
# 不为数字的内容都转换成0，用列表解析可以这样写：
a = ['1', '2', '3', 'i', '8']
print([int(i) if i.isdigit() else 0 for i in a])

# 获取一个全0列表, 有时候我们可能需要获取一个长度指定，全零或者全为某个值列表：
print(['ok' for i in range(10)])

# 略复杂的列表解析，获取列表中嵌套列表的元素，生成一个无嵌套的新列表
# 这个例子说起来挺拗口，实际上是想从[[1,2],[3,4,5],[6,7]，[8]]这种列表中，把嵌套在列表中的元素解出来，
# 得到[1,2,3,4,5,6,7,8]，用列表解析可以这样写：
a = [[1, 2], [3, 4, 5], [6, 7], [8]]
print([x for i in a for x in i])

# 获取笛卡尔积
a = ['4k', '8k', '12k']
b = ['1', '2,', '3']
c = ['libaio', 'bio', 'directio']
print([{'blocksize': x, 'numjobs': y, 'ioengine': z}
      for x in a for y in b for z in c])

# 获取所有可能的组合
# 假设有一个配置列表['a','b','c'],我们想获取所有的由a,b,c组成的字符串（可以重复使用，将顺序也考虑在内），
# 列表解析需要配合itertools中的product函数：
from itertools import product
x = ['a', 'b', 'c']
results = ["".join(i) for i in product(x, repeat=3)]
print(results)

# 矩阵转置
# 考虑一个矩阵，matrix=[[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12]]，
# 现在要获得他的转置矩阵，用列表解析仍然是一行：
import os
import sys
import math
transposed = [list(row) for row in zip(*matrix)]
print(transposed)