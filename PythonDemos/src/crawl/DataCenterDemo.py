#!/usr/bin/python
# coding:utf8
'''
Created on 2017-4-12
请求4.0分析系统
@author: dh
'''
import urllib2
import urllib
# 登录
def login():
    loginURL = 'http://localhost:8080/DC_161110/login.do'
    user = {'un':'user', 'pa':'123456'}
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
    return jsession 

# 查询    JSESSIONID=B079D76FDD9F91E8E854358EB7E6B076
def search():
    jsession = login()
    print jsession
    searchURL = 'http://localhost:8080/DC_161110/storeSearch.do'
    data = {'size':'50', 'fieldValue':'测试'}
    data = urllib.urlencode(data)
    header = {
        'Cookie':jsession
    }
    request = urllib2.Request(searchURL, data=data, headers=header)
    print request
    response = urllib2.urlopen(request)
    print response.read()
search()























































