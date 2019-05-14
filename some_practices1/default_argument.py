#!/usr/bin/python3

def printinfo(name, age = 35):
    '打印任何传入的字符串'
    print('名字：', name)
    print('年龄：', age)
    return
#调用printinfo函数
printinfo(age=50, name='runoob')
print('-----------------------')
printinfo(name='runoob')