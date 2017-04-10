#!/usr/bin/python
# coding:utf8
'''
Created on 2017-4-10
面向对象编程
@author: dh
'''
# 表示继承自object
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    # 第一个参数永远是self,调用时不要传递该参数
    
    def printScore(self):
        print "%s的分数：%s" % (self.name, self.score)
    def get_score(self):
        return self.score
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer')
        if value < 0 or value > 100:
            raise ValueError('score must be in 0-100')
        self.score = value

s1 = Student('admin', 0)
s1.set_score(30)
print s1.get_score()


#import types
#print type('134') == types.StringType
