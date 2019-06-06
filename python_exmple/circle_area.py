#!/usr/bin/python3
# filename : circle area
# author by : BlaineXu


def findArea(r):
    # r = float(input('Please input your circle radius: '))
    PI = 3.142
    return PI * (r * r)


print("圆的面积为 %.6f" % findArea(5))
