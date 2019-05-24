#!/usr/bin/python3

def this_fail():
    x = 1/0

try:
    this_fail()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
