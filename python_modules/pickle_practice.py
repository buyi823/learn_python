#!/usr/bin/python3
import pprint, pickle

# 使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
print(data1)

print('-----------------')
data2 = pickle.load(pkl_file)
print(data2)
data3 = pickle.load(pkl_file)
print(data3)

pkl_file.close()