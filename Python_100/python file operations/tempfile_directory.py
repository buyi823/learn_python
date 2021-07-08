#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# tempfile 也可用于创建临时目录。 让我们看一下如何使用 tempfile.TemporaryDirectory()来做到这一点

import tempfile
import os

tmp = ''
with tempfile.TemporaryDirectory() as tmpdir:
    print('Created temporary directory: ', tmpdir)
    tmp = tmpdir
    print(os.path.exists(tmpdir))

print(tmp)
print(os.path.exists(tmp))