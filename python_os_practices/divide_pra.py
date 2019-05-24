#!/usr/bin/python3

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print('division by zero!')
    else:
        print('result is', result)
    finally:
        print('executing finally clause')
        
    print(divide(2,0))
