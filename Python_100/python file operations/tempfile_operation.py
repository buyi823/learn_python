#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# tempfile 可以在你程序运行时打开并存储临时的数据在文件或目录中。 
# tempfile 会在你程序停止运行后删除这些临时文件。

from tempfile import TemporaryDirectory, TemporaryFile

# 创建一个临时文件并为其吸入一些数据
fp = TemporaryFile('w+t')
fp.write('Hello World!')
# 回到开始，从文件中读取数据
fp.seek(0)
data = fp.read()
print(data)
# 关闭文件，之后他将会被删除
fp.close()

# .TemporaryFile() 也是一个上下文管理器，因此它可以与with语句一起使用。
#  使用上下文管理器会在读取文件后自动关闭和删除文件：
# with TemporaryFile('w+t') as fp:
#     fp.write('Hello World!')
#     fp.seek(0)
#     fp.read()