#!/user/bin/python3
# -*- coding: UTF-8 -*-
# 使用 glob 进行文件名模式匹配

import glob
from pathlib import Path

for name in glob.glob('*[0-9]*.txt'):
    print(name)

print('===================================')

# 这里例子使用了 glob.iglob() 在当前目录和子目录中搜索所有的 .py 文件。
# 传递 recursive=True 作为 .iglob() 的参数使其搜索当前目录和子目录中的 .py 文件。
# glob.glob() 和 glob.iglob() 不同之处在于，iglob() 返回一个迭代器而不是一个列表

for name1 in glob.iglob('**/*.py', recursive=True):
    print(name1)

print('===================================')

# pathlib 也包含类似的方法来灵活的获取文件列表。
# 下面的例子展示了你可以使用 .Path.glob() 列出以字母 p 开始的文件类型的文件列表。

p = Path('.')

for name2 in p.glob('*.p*'):
    print(name2)
#调用 p.glob('*.p*') 会返回一个指向当前目录中所有扩展名以字母 p 开头的文件的生成器对象。