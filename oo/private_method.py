#!/usr/bin/python


class Site:
    def __init__(self, name, url):
        self.name = name  # public
        self.__url = url  # private

    def who(self):
        print('name : ', self.name)
        print('url : ', self.__url)

    def __foo(self):  # private method
        print('this is a private method')

    def foo(self):  # public method
        print('this is a public method')
        self.__foo()


x = Site('rookie lession', 'www.runoob.com')
x.who()  # regular print
x.foo()  # regular print
# x.__foo()       报错 外部不能调用私有方法