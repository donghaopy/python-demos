#! /usr/bin/env python
# _*_coding:utf-8 _*_
'''
Created on 2017-3-7

@author: dh
'''
# 条件判断和循环
names = ('jame', 'bryant', 'jordan')
for name in names:
    print name
# range
sum = 0
values = range(5)
for value in values:
    sum += value
print sum
# 遍历字典
dic = {'name':'donghao', 'age':28}
for k , v in dic.items():
    print k, v
    
