#!/usr/bin/python

# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self
class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()