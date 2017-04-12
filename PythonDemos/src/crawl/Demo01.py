# coding:utf8
'''
Created on 2017年4月10日
爬虫
@author: Administrator
'''
import re
import urllib2
import traceback

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# 加上User-Agent，表明你是浏览器访问
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    # print html
    # 正则最好先编译
    # 非贪婪匹配
    pattern = re.compile('<div\sclass="content">.*?</div>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        print '匹配结果:\r\n', item
        
# 打印异常     
except Exception, e:
    print 'str(Exception):\t', str(Exception)
    print 'str(e):\t\t', str(e)
    print 'repr(e):\t', repr(e)
    print 'e.message:\t', e.message
    print 'traceback.print_exc():'; traceback.print_exc()
    print 'traceback.format_exc():\n%s' % traceback.format_exc()
