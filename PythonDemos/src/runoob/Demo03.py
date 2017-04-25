#!/usr/bin/python
# coding:utf8
'''
Created on 2017-4-17
爬取runoob页面
@author: dh
'''
import requests
import HTMLParser
from pyquery import PyQuery

# 读取文件内容
def read_file(file_name):
    file = open(file_name, 'r')
    txt = file.read()
    file.close()
    return txt
# 转义
def parser(html):
    html_parser = HTMLParser.HTMLParser()
    txt = html_parser.unescape(html) 
    return txt

# 爬取某一页面，并用pyquery处理
def get_page():
    response = requests.get('http://www.runoob.com/python/python-chinese-encoding.html')
    html = response.text
    pyhtml = PyQuery(html)
    
    # 插入js代码 append
    css = read_file('d:/total.css')
    pyhtml('head').after('<style>' + css + '</style>')
    # 插入css代码 append
    js = read_file('d:/total.js')
    pyhtml('head').append('<script>' + js + '</script>')
    
    for link in pyhtml('link').items():
        cssHref = link. attr('href')
        if '.css' in cssHref:
            # 移除标签
            pyhtml(link).remove()
        
    
    for src in pyhtml('script').items():
        scriptUrl = src.attr('src')
        if scriptUrl is not None and '.js' in scriptUrl:
            # 移除标签
            pyhtml(src).remove()
    
    
    
    # pyhtml('head').after("\r\n<link rel='stylesheet' href='./total.css' />\r\n")
    # pyhtml('head').after("\r\n<script src='./total.js'></script>\r\n")
    
    file = open('d:/python-chinese-encoding.html', 'w')
    content = str(pyhtml)
    file.write(parser(content))
    file.close()

get_page()


def test_pyquery():
    htmljs = '''
        <head></head>
        <link rel='stylesheet' href='//cdn.bootcss.com/font-awesome/4.7.0/css/font-awesome.min.css' media='all' />
        <script src='2.js'></script>
    '''
    pyhtml = PyQuery(htmljs)
    # 追加內容
    pyhtml('head').append("<span>dongdidi</span")
        
    print str(pyhtml)

# test_pyquery()


    
# print read_file('d:/total.css')
# print '------------------------------------------------------------'
# print read_file('d:/total.js')






























