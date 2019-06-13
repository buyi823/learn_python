#!/usr/bin/python3
# 移除字典点键值(key/value)对
# 使用 del 移除
test_dict={"Runoob" : 1, "Google" : 2, "Taobao" : 3, "Zhihu" : 4}

print("字典移除前 : "+ str(test_dict))

del test_dict['Zhihu']

print("字典移除后 : " + str(test_dict))

# 移除没有的 key 会报错
#del test_dict['Baidu']