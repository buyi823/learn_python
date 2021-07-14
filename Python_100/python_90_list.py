#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-07-14 15:07
# list

matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix)
print(matrix[1])
col2 = [row[1] for row in matrix] #get a  column from a matrix  
print(col2)
coleven = [row[1] for row in matrix if row[1] % 2 == 0]
print(coleven)