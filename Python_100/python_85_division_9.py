#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-07-28 16:24
# 题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。程序分析：999999 / 13 = 76923。

if __name__ == '__main__':
    zi = int(input('input a number:\n'))
    n1 = 1
    c9 = 1
    m9 = 9
    sum = 9
    while n1 != 0:
        if sum % zi == 0:
            n1 = 0
        else:
            m9 *= 10
            sum += m9
            c9 += 1
    print('%d 个9可以被 %d 整除' % (c9, zi))
    r = sum / zi
    print('%d / %d = %d' % (sum, zi, r))

# 程序有个缺陷，如果输入5，不能被任何几个9整除，那么程序不能执行也不会退出
# 运行结果：
# input a number:
# 13
# 6 个9可以被 13 整除
# 999999 / 13 = 76923
