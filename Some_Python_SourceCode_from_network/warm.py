#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-12-17 14:16
# happy birthday to you

list(map(lambda x: print("Happy Birthday to " + ("you!" if x != 2 else "Rachael!")), range(4)))

from turtle import*

penup()
goto(0,-200)
pendown()
circle(200)
fillcolor('blue')
penup()
goto(-100, 50)
pendown()
begin_fill()
circle(20)
end_fill()
penup()
goto(100,50)
pendown()
begin_fill()
circle(20)
end_fill()
penup()
goto(0,50)
pendown()
circle(-50,steps=3)
penup()
goto(-150,-70)
pendown()
goto(0,-170)
goto(150,-70)
