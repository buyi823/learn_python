#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-12-15 18:19
# Draw rainbow line

import turtle

q = turtle.Pen()
turtle.bgcolor("black")
sides = 7
colors =["red","orange","yellow","green","cyan","blue","blue","purple"]
for x in range(360):
    q.pencolor(colors[x%sides])
    q.forward(x*3/sides+x)
    q.left(360/sides+1)
    q.width(x*sides/200)