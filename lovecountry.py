#!/usr/bin/python3
from turtle import *

setup(600,400,0,0) #设定大小，四个参数：宽度、高度、起始点X值，Y值
bgcolor('red')  # 背景色红色
fillcolor('yellow') #线条及填充颜色设为黄色
color('yellow')
speed(8) # 画笔运行速度

begin_fill() #开始填充
up() # 提起画笔，此时移动画笔不会进行绘画
goto(-280,100) # 前往坐标
down() #放下画笔，此时移动画笔，直接进行绘画
for i in range(5):
    fd(150) #forward的简写，意思为向前移动画笔150单位
    rt(144) # right的简写，向右旋转144度（重复5次）
end_fill()

#四顆小五角星部分
begin_fill() #開始填充
up()
goto(-100,180)
setheading(305)
down()
for i in range(5):
    fd(50)
    lt(144)
end_fill()

#其餘三顆小五角星
begin_fill()
up()
goto(-50,110)
setheading(30)
down()
for i in range(5):
    fd(50)
    rt(144)
end_fill()

begin_fill()
up()
goto(-40,50)
setheading(5)
down()
for i in range(5):
    fd(50)
    rt(144)
end_fill()

begin_fill()
up()
goto(-100,10)
setheading(300)
down()
for i in range(5):
    fd(50)
    lt(144)
end_fill()
