#!/usr/bin/python3
# 移除字典点键值(key/value)对
# 使用 item() 移除
# 字典(Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组

test_dict = {"Runoob" : 1, "Google" : 2, "Taobao" : 3, "Zhihu" : 4} 
  
# 输出原始的字典
print ("字典移除前 : " + str(test_dict)) 

# 使用 pop 移除 Zhihu
new_dict = {key:val for key, val in test_dict.items() if key != 'Zhihu'}

print ("字典移除后 : " + str(new_dict))

