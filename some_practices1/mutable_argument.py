#!/usr/bin/python3

def printinfo(arg1, *vartuple):
    '打印任何传入的参数'
    print('输出： ')
    print(arg1)
    print(vartuple)

#调用printinfo
printinfo(70,60,50)