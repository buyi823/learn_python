#!/usr/bin/python3

num = 1
def fun1():
    global num
    print(num)
    num = 123
    print(num)
fun1()
print(num)