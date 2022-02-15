#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-12-17 14:43
# draw heart

print('\n'.join([''.join([('XuZiHan'[(x-y)%7]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))