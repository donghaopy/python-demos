#! /usr/bin/env python
#_*_coding:utf-8 _*_
'''
Created on 2017-3-6

@author: 董昊
'''
print("hello python")

name=raw_input("please enter your name:")
print 'hello,',name
#转int类型
value=raw_input("please enter your value:")
value=int(value)
if(value>0):
    print value
else:
    print (-value)
