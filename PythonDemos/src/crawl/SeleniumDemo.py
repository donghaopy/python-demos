# coding:utf8
'''
Created on 2017-4-13
使用selenium模拟用户行为
将chrome的驱动放到 D:\Python27\Scripts目录下面
@author: dh
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class SeleniumTest(unittest.TestCase):
    def setUp(self):
        global driver
        driver = webdriver.Chrome()
    # 测试
    def test_searchPython(self):
        driver.get('http://www.python.org')
        self.assertIn('Python.org', driver.title)
        # 关键字搜索
        element = driver.find_element_by_name("q")
        '''
            python会自动解码，但是解码sys.defaultencoding 是 anscii，所以要指定解码为utf-8
        '''
        s='测试'
        element.send_keys(s.decode('utf-8'))
        element.send_keys(Keys.RETURN)
        print driver.page_source
    def tearDown(self):
        driver.close()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    