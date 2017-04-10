#!/usr/bin/python
# coding:utf8
'''
Created on 2017-4-10
处理异常
@author: dh
'''
import types
# 打印日志
import logging
logging.basicConfig(level=logging.INFO)
# 使用断言
assert type('123') == types.StringType
# 处理异常
try:
    # print 'try....'
    r = 10 / int(raw_input('please enter number：'))
    logging.info(r);
except ValueError, e:
    logging.error('%s,%s' % ('ValueError', e))
except ZeroDivisionError, e:
    logging.error('%s,%s' % ('ZeroDivisionError', e))
finally:
    logging.info('finally...');
    
