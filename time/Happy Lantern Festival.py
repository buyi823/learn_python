#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine(I just copied the code)
# Time: 2022-02-15 19:18:25
# Description: Happy Lantern Festival

import wxgl.wxplot as plt

plt.title('江天一色无纤尘，皎皎空中孤月轮' + '^_^' + 'Happy Lantern Festival')
# plt.title('Happy Lantern Festival')

plt.uvsphere((0,0,0), 1, 
    lon= (0,360), 
    lat= (90, -90), 
    texture=r'C:\Users\30952\Desktop\moon.jpg', 
    transform = lambda duration : ((0, 1, 0, (0.02*duration)%360),),
    light = None)
plt.text('众里寻他千百度，', pos=(1.2,-0.3,0), size=128)
plt.text('蓦然回首，', pos=(1.2,-0.5,0), size=128)
plt.text('那人却在灯火阑珊处。', pos=(1.2,-0.7,0), size=128)
plt.show()