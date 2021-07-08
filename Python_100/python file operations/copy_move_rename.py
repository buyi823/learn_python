#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-07-07 14:47
# copy move and rename file & directory

import shutil

# shutil 提供了一些复制文件的函数。 最常用的函数是 shutil.copy() 和 shutil.copy2() 。
# 使用shutil.copy() 将文件从一个位置复制到另一个位置，请执行以下操作：
src = 'C:\\Users\\Blaine\\Desktop\\send mail.txt'
dst = 'D:\\buyi_prac\\Python_100\\python file operations\\'
shutil.copy(src, dst)
# shutil.copy() 仅复制文件的内容和文件的权限。 其他元数据（如文件的创建和修改时间）不会保留。
# 要在复制时保留所有文件元数据，请使用 shutil.copy2()
# 例如上面的我从桌面将文件复制到D盘，使用copy那D盘文件的时间就是复制的时间；
# 使用copy2()复制的话，复制到D盘就保留了桌面文件的原始信息
shutil.copy2(src, dst)

shutil.copytree('c:/Users/Blaine/Desktop/test', 'd:/test')
# 目标目录不能时已经存在的目录，它将被创建而不带有其父目录

shutil.move('C:/Users/Blaine/Desktop/send mail.txt', 'd:/')
shutil.move('c:/Users/Blaine/Desktop/Test', 'd:/')
# 移动目录或者文件到目标地址

