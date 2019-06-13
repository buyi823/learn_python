#!/usr/bin/python3
#  按键(key)或值(value)对字典进行排序

lis = [{ "name" : "Taobao", "age" : 100},  
{ "name" : "Runoob", "age" : 7 }, 
{ "name" : "Google", "age" : 100 }, 
{ "name" : "Wiki" , "age" : 200 }] 

# 通过age升序排列
print('列表通过age升序排列: ')
print(sorted(lis, key = lambda i: (i['age'], i['name'])))

print('\r')

# 按age降序排列
print ("列表通过 age 降序排序: ")
print (sorted(lis, key = lambda i: i['age'],reverse=True))