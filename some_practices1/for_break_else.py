#!/usr/bin/python3
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print('菜鸟教程')
        break
    print('数据循环 '+ site)
else:
    print('没有数据循环')
print("完成循环")