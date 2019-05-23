#!/usr/bin/python3

import os,stat

path = "D:\\buyi_github_project\\learn_python\\python_os_practices\\foo.txt"

# 为文件设置标记，使得它不能被重命名和删除
flags = stat.SF_NOUNLINK
retval = os.chflags( path, flags )
print ("返回值: %s" % retval)