#!/usr/bin/python
# coding:utf8
'''
Created on 2017-4-11
使用ThreadLocal
@author: dh
'''
import threading
local_school = threading.local()
def process_student():
    print 'hello,%s(in %s)' % (local_school.student, threading.current_thread().name)
def process_thread(name):
    local_school.student = name
    process_student()
    
t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
