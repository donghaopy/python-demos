# coding:utf8
'''
Created on 2017-4-10
使用文档测试,直接python Demo03.py或者Run As Python Run
@author: dh
'''
def abs(n):
    '''
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)
# 引入
import doctest
doctest.testmod()
