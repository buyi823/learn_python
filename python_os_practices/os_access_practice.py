#!/usr/bin/python3

import os, sys
# 假定foo.txt存在，并有读写权限

ret = os.access("D:\\buyi_github_project\\learn_python\\python_os_practices\\foo.txt", os.F_OK)
print('F_OK - 返回值 %s' % ret)

ret = os.access("D:\\buyi_github_project\\learn_python\\python_os_practices\\foo.txt", os.R_OK)
print('R_OK - 返回值 %s' % ret)

ret = os.access("D:\\buyi_github_project\\learn_python\\python_os_practices\\foo.txt", os.W_OK)
print('W_OK - 返回值 %s' % ret)

ret = os.access("D:\\buyi_github_project\\learn_python\\python_os_practices\\foo.txt", os.X_OK)
print('X_OK - 返回值 %s' % ret)
