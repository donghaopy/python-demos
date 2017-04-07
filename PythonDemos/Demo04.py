#!/usr/local/env python
# _*_coding:utf-8 _*_
'''
编写map-reduce函数

Created on 2017-4-7
@author: dh
'''
def fn(x, y):
    return x * 10 + y
def char2num(s):
    # 取字典中的值
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# print char2num('1')
# 使用map函数返回是一个list结构
print map(char2num, '13579')
# 使用reduce函数处理list集合
print reduce(fn, map(char2num, '13579'))

# 整理成一个str2int函数
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        # 取字典中的值
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
print str2int('12345')
