#! /usr/bin/env python
# _*_coding:utf-8 _*_
'''
Created on 2017-3-6

@author: 董昊
'''
# 导入模块
import Demo05
# 导入包
import map.Demo04
# 使用模块中的方法
Demo05.capitalize_map(['aBC', 'ABC', 'abc'])
# 使用包中的方法
print map.Demo04.str2int('1234456')

print("hello python")

name = raw_input("please enter your name:")
print 'hello,', name
# 转int类型
value = raw_input("please enter your value:")
value = int(value)
if(value > 0):
    print value
else:
    print (-value)
