#!/usr/bin/python3

def sum(arg1, arg2):
    total = arg1 + arg2
    print('函数内: ', total)
    return total

total = sum(10,20)
print('函数外: ', total)