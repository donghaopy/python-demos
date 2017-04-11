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
#    ()：代表分组

s = '''hello src=java yes 
no python 
hello src=python yes
 hadoop hbase hive'''
r = r"hello src=.+ yes"
print re.findall(r, s)
#    ()优先获得里面的值
r = r"hello src=(.+) yes"
print re.findall(r, s)
#    添加?非贪婪匹配
s = '<H1>Chapter 1 - 介绍正则表达式</H1>'
#    不加?则匹配所有
#    .匹配单个字符
r = r'<.*?>'
print re.findall(r, s)

#使用Eclipse Regex替换：$0代表匹配第几个分组
#([0-9])、--->>>1$0





















