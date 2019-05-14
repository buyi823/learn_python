#!/usr/bin/python3

def printinfo(arg1, **vardict):
    print('输出： ')
    print(arg1)
    print(vardict)

printinfo(1,a=2,b=3)