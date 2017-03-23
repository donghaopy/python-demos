#! /usr/bin/env python
#_*_coding:utf-8 _*_
'''
Created on 2017-3-6

@author: dh
'''
#list与tuple
classmates=['donghao','ruandi','xiongmao']
#长度
print(len(classmates))

print(classmates[0])
print(classmates[1])
print(classmates[2])
#追加
classmates.append('jordan')
print(classmates[3])
#insert
classmates.insert(0, 'james')
print(classmates)
#pop在0位移除
classmates.pop(0)
print(classmates)
#tuple：理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。
t=('james','jordan')
print(t[0])