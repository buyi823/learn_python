#!/usr/bin/python3
# 判断元素是否在列表中存在

from bisect import bisect_left

# init list
test_list_set = [1,6,3,5,3,4]
test_list_bisect = [1,6,3,5,3,4]

print("查看 4 是否在列表中 ( 使用 set() + in) : ")

test_list_set = set(test_list_set)
if 4 in test_list_set:
    print('存在')

print("查看 4 是否在列表中 ( 使用 sort() + bisect_left() ) : ") 

test_list_bisect.sort()
if bisect_left(test_list_bisect, 4):
    print('存在')