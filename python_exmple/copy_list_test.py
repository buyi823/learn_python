#!/usr/bin/python
# copy list

def clone_runoob(li1):
    li_copy = []
    li_copy.extend(li1)
    # extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
    return li_copy

li1 = [4, 8, 2, 10, 15, 18] 
li2 = clone_runoob(li1)
print("原始列表:", li1) 
print("复制后列表:", li2) 