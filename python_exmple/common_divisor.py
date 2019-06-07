#!/usr/bin/python3
# common divisor 公约数


def hcf(x, y):
    """该函数返回两个数的最大公约数"""
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf


num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

print(num1, "and", num2, 'common divisor is: ', hcf(num1, num2))
