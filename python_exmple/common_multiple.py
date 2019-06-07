#!/usr/bin/python3
# filename: common multiple


def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

print(num1, "and", num2, "common multiple is: ", lcm(num1, num2))