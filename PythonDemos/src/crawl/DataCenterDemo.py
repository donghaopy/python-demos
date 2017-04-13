#!/usr/bin/python
# coding:utf8
'''
Created on 2017-4-12
请求4.0分析系统
@author: dh
'''
import urllib2
import urllib
import requests

loginURL = 'http://localhost:8080/DC_161110/login.do'

searchURL = 'http://localhost:8080/DC_161110/storeSearch.do'

user = {'un':'admin', 'pa':'123456'}
    
# 登录
def login():
    # 编码
    data = urllib.urlencode(user)
    # print data
    request = urllib2.Request(loginURL, data=data)
    response = urllib2.urlopen(request)
    # 获得session
    jsession = response.headers['Set-cookie']
    jsession = jsession[jsession.index('JSESSIONID'):jsession.index(';')]
    # print response.getcode()
    # response是socket._fileobject对象
    # print response.read()
    print jsession
    return jsession 

# 查询
def search():
    data = {'size':'50', 'fieldValue':'测试'}
    data = urllib.urlencode(data)
    header = {
        'Cookie':requests_Login()
    }
    request = urllib2.Request(searchURL, data=data, headers=header)
    response = urllib2.urlopen(request)
    print response.read()

# 使用requests模块
def requests_Login():
    response = requests.post(loginURL, data=user)
    for key, value in response.request._cookies.iteritems():
        return '%s=%s' % (key, value)
    
# 查询成功
search()





















































