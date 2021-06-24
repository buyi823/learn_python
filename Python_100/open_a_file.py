#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# open file and read it

with open('data.txt', 'r') as f:
    data = f.read()
    print('context:{}'.format(data))