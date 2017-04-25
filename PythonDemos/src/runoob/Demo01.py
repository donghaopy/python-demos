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

# 爬取某一页面，并用pyquery处理
def get_page():
    response = requests.get('http://www.runoob.com/python/python-chinese-encoding.html')
    # return response.text
    file = open('d:/python-chinese-encoding.html', 'w')
    html = response.text
    pyhtml = PyQuery(html)
    for link in pyhtml('link').items():
        # 替换掉css标签
        cssHref = link. attr('href')
        if '.css' in cssHref:
            style = '<style>' + get_css(cssHref) + '</style>'
            link.replace_with(style)
        else:
            pass
    
    for src in pyhtml('script').items():
        # 替换掉javascript内容
        scriptUrl = src.attr('src')
        if scriptUrl is not None :
            newitem = src.remove_attr('src').text(get_script(scriptUrl))
            src.replace_with(newitem)
    # 转义
    result = parser(str(pyhtml))
    file.write(result)
    file.close()

#处理css内容
def get_css(cssHref):
    if not cssHref.startswith("//"):
        href = "http://" + 'www.runoob.com' + cssHref
    else:
        href = "http:" + cssHref
    print '正在下载css文件',href
    response = requests.get(href)
    return response.text

# 获得JavaScript脚本内容  
def get_script(scriptUrl):
    print '正在下载url', scriptUrl
    if not scriptUrl.startswith("//") and not '.php' in scriptUrl:
        # 以/开头的需要添加网站域名
        url = "http://" + 'www.runoob.com' + scriptUrl
    elif '.php' in scriptUrl:
        url=scriptUrl
    else:
        url = "http:" + scriptUrl
        
    response = requests.get(url)
    
    return response.text

#转义
def parser(html):
    html_parser = HTMLParser.HTMLParser()
    txt = html_parser.unescape(html) 
    return txt

def test1():
    response = requests.get('http://www.runoob.com/python/python-chinese-encoding.html')
    file = open('d:/python-chinese-encoding.html', 'w')
    file.write(response.text)
    file.close()
test1()

