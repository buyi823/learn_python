#!/usr/bin/python3
# reverse list


def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst


lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))