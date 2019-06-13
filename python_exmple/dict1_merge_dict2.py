#!/usr/bin/python3
# 合并字典

def Merge(dict1, dict2):
    return(dict2.update(dict1))
    # 字典(Dictionary) update() 函数把字典dict2的键/值对更新到dict里

# 两个字典
dict1 = {'a': 10, 'b': 8} 
dict2 = {'d': 6, 'c': 4} 

# return None
print(Merge(dict1,dict2))

# dict2 merge dict1
print(dict2)