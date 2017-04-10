#!/usr/bin/python
# coding:utf8
'''
Created on 2017-4-10

@author: dh
'''
# 使用@property定义属性
class Student1(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, value):
        self._birth = value
    def printBirth(self):
        return "Student1的birth：", self._birth
    def __str__(self):
        return "toString()方法："
s2 = Student1()
print s2
# setter方法
s2.birth = 30
# getter方法
print s2.birth
print s2.printBirth()

# 链式调用
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

print Chain().status.user.timeline.list



















