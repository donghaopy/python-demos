#!/usr/local/env python
# _*_coding:utf-8 _*_
'''
Created on 2017-4-7

@author: dh
'''
# map()函数把一个函数应用于序列中所有项，并返回一个列表
def capitalize_map(s):
    def capitalize(s):
        s_len = len(s)
        first = s[0].upper()
        second = s[1:s_len].lower()
        return first + second
    return map(capitalize, s)

print capitalize_map(['aBC', 'ABC', 'abc'])

# lambda匿名函数
g = lambda x, y:x + y
print g(2, 3)

# filter
print filter(lambda n:n % 2 == 1, (1, 2, 3, 4, 5))
# sorted
print sorted((3, 1, 4, 2, 5))

# list赋值
f1, f2, f3 = [1, 2, 3]
print 'f1:', f1
print 'f2:', f2
print 'f3:', f3

# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i * i
        # fs append 的是函数
        fs.append(f)
    return fs
# count里面的每个值分别付给三个变量
f1, f2, f3 = count()

print f1()
print f2()
print f3()

# 偏函数：能够固定住原函数的部分参数
import functools
def auh(n, m):
    return n + m
auh2 = functools.partial(auh, 100)
print auh(20, 100)==auh2(20)

