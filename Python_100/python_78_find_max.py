#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-08-04 17:09
# 找出年龄最大

if __name__ == '__main__':
    person = {"li":18, "wang":50, "zhang":20, "sun":22}
    m = 'li'
    for key in person.keys():
        if person[m] < person[key]:
            m = key
            
    print('%s, %d' % (m, person[m]))