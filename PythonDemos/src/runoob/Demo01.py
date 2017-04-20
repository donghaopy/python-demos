#!/usr/bin/python
# coding:utf8
'''
Created on 2017-4-17
爬取runoob页面
@author: dh
'''
import requests
from pyquery import PyQuery

def get_page():
    response = requests.get('http://www.runoob.com/python/python-tutorial.html')
    # return response.text
    # file = open('d:/python-tutorial.html', 'w')
    html = response.text
    pyhtml = PyQuery(html)
    for href in pyhtml('link').items():
        #替换掉css标签
        pass
    for src in pyhtml('link').items():
        #替换掉javascript内容
        pass
    
    # file.write(response.text)
    # file.close()
    
def get_script():
    http = "http:"
    response = requests.get(http + '//cdn.bootcss.com/jquery/2.0.3/jquery.min.js')
    return response


# get_page()

def test_pyquery():
    htmljs = "<link href='1.css' /><script src='3.js'></script><link href='2.css' /><link href='3.css' /><script src='4.js'></script>"
    pyhtml = PyQuery(htmljs)
    # html = str(pyhtml('script'))
    # 遍历
    for item in pyhtml('script').items():
        # 替换掉该标签中的内容
        newitem=item.remove_attr('src').text("function(){}")
        item.replace_with(newitem)
        
        
    print str(pyhtml)
    
def test_getjs():
    response = requests.get('http://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js')
    print response.text
        
test_getjs()
