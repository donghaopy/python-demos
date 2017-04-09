#!/usr/local/env python
# _*_coding:utf-8 _*_
'''
Created on 2017-4-7

@author: dh
'''
#map()函数把一个函数应用于序列中所有项，并返回一个列表
def capitalize_map(s):
    def capitalize(s):
        s_len=len(s)
        first=s[0].upper()
        second=s[1:s_len].lower()
        return first+second
    return map(capitalize, s)

print capitalize_map(['aBC','ABC','abc'])

#lambda匿名函数
g=lambda x,y:x+y
print g(2,3)

