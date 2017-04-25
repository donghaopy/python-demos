#coding:utf8
'''
Created on 2017-4-25
html字符转义
@author: dh
'''
import HTMLParser
html = '&#32534;&#30721;'
#转义
def parser():
    html_parser = HTMLParser.HTMLParser()
    txt = html_parser.unescape(html) 
    return txt

print parser()

#反转义
import cgi
print cgi.escape('<abc>')