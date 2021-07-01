#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Python可以很轻松的获取文件大小和修改时间等文件属性。
# 可以通过使用 os.stat() ， os.scandir() 或 pathlib.Path 来获取

import os, datetime
from pathlib import Path


with os.scandir('D:/buyi_prac/Python_100') as entries:
    for entry in entries:
        info = entry.stat()
        print(info.st_mtime) # 以时间戳的方式输出

# 在上面的例子中，循环 .iterdir() 返回的迭代器并通过对其中每一项调用 .stat() 来获取文件属性。
# st_mtime 属性是一个浮点类型的值，表示的是时间戳。为了让 st_time 返回的值更容易阅读，
# 你可以编写一个辅助函数将其转换为一个 datetime 对象：


def timestamp2datetime(timestamp, convert_to_local=True, utc=8, is_remove_ms=True):
    """                                                                           
    转换 UNIX 时间戳为 datetime对象                                                       
    :param timestamp: 时间戳                                                         
    :param convert_to_local: 是否转为本地时间                                             
    :param utc: 时区信息，中国为utc+8                                                     
    :param is_remove_ms: 是否去除毫秒                                                   
    :return: datetime 对象                                                          
    """                                                                           
    if is_remove_ms:                                                              
        timestamp = int(timestamp)                                                
    dt = datetime.datetime.utcfromtimestamp(timestamp)                            
    if convert_to_local:                                                          
        dt = dt + datetime.timedelta(hours=utc)                                   
    return dt                                                                     


def convert_date(timestamp, format='%Y-%m-%d %H:%M:%S'):                          
    dt = timestamp2datetime(timestamp)                                            
    return dt.strftime(format)                                                    


basepath = Path('D:/buyi_prac/Python_100')                                                   
for entry in basepath.iterdir():
    if entry.is_file():
        info = entry.stat()                                                           
        print('{} 上次修改时间为 {}'.format(entry.name, timestamp2datetime(info.st_mtime)))