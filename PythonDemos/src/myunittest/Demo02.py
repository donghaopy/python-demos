# coding:utf-8
'''
>>> abs(1)
1
Created on 2017-4-10
使用单元测试、文档测试
@author: dh
'''
# 自定义字典类
class Dict(dict):
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)
    def __getattr__(self, key):
       try:
           return self[key]
       except:
           raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value

# 使用单元测试
import unittest
# 定义测试类继承自unittest.TestCase
class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(name='admin', age=30)
        self.assertEqual(d.name, 'admin')
    def test_key(self):    
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
# 使用文档测试
import doctest
doctest.testmod()       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
