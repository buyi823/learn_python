#!/usr/bin/python
#-*- coding: UTF-8 -*-
# write some date to the file

with open('data.txt', 'w') as f:
    data = 'some data to be written to the file'
    f.write(data)