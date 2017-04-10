# coding:utf-8
'''
Created on 2017年4月9日
正则表达式
@author: Administrator
'''
#    []：表示匹配一个或多个字符集,元字符不起作用
#    ^：表示匹配行首,$：表示匹配行尾
#    重复：{8}重复8次,*表示重复它前面的字符0-n次,+至少1次,?表示可有可无
import re
r = '[0-9]'
print re.findall(r, '1 a 9')

r = 'ab+'
print re.findall(r, 'a')
print re.findall(r, 'ab')

r = '^010-?\d{8}$'
print re.findall(r, '010-12345678')
print re.findall(r, '01012345678')
# 不匹配    print re.findall(r, '010--12345678')
#    {m,n}：至少重复m次,最多重复n次
#    在开头加r是对反斜杠不做特殊处理





















