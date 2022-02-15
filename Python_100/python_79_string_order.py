#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-08-04 16:43
# string order

if __name__ == '__main__':
    str1 = input('input string:\n')
    str2 = input('input string:\n')
    str3 = input('input string:\n')
    print(str1, str2, str3)

    if str1 > str2:
        str1, str2 = str2, str1
    if str1 > str3:
        str1, str3 = str3, str1
    if str2 > str3:
        str2, str3 = str3, str2

    print('after being sorted.')
    print(str1, str2, str3)
'''
在python中，默认是按照ascii的大小比较的； 字符串按位比较，
两个字符串第一位字符的ascii码谁大，字符串就大，不再比较后面的； 
第一个字符相同就比第二个字符串，以此类推。 
注意：空格的ascii码是32，空（null）的ascii码是0，大写字母和小写字母的ascii不同
'''