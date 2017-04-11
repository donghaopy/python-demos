# !/user/bin/pyhton
# coding:utf8
'''
Created on 2017-4-11
xml解析百度天气
@author: dh
'''
import urllib
import re
from xml.parsers.expat import ParserCreate

xml = ''
try:
    page = urllib.urlopen('http://api.map.baidu.com/telematics/v2/weather?location=%E4%B8%8A%E6%B5%B7&ak=B8aced94da0b345579f481a1294c9094')
    xml = page.read()
finally:
    page.close()

# print xml

class BaiduWeatherSaxHandler(object):
    def __init__(self):
        self._weather = dict()
        self._count = 0
        self._current_element = ''
    def start_element(self, name, attr):
        if name == 'result':
            self._count += 1
            self._weather[self._count] = dict()
        self._current_element = name
    def end_element(self, name):
        pass
    def char_data(self, text):
        # 排除换行符和空白内容
        re_str = '^[\n|\s]+$'
        if self._current_element and not re.match(re_str, text) and self._weather:
            self._weather[self._count][self._current_element] = text
            
    def show_weather(self):
        for v in self._weather.values():
            print '日期:%s,天气:%s,风力:%s,温度:%s' % (v['date'], v['weather'], v['wind'], v['temperature'])
            # print v['date'], '\t'*(7-len(v['date'])), v['temperature'], v['weather'], v['wind']
    
baidu = BaiduWeatherSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = baidu.start_element
parser.EndElementHandler = baidu.end_element
parser.CharacterDataHandler = baidu.char_data
parser.Parse(xml)
# 显示天气
baidu.show_weather()


















