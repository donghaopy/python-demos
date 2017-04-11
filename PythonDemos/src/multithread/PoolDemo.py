#!/usr/bin/python
# coding:utf8
'''
Created on 2017-4-11
多进程
@author: dh
'''
# 进程池创建批量子进程
# 单核多线程主要就是针对阻塞这种情况能提高效率，如果要利用多核的话应该用多进程
# from multiprocessing.pool import Pool
import os, time, random
# 注意不要与Python中的模块重名
from multiprocessing import Pool

def long_time_task(name):
        print 'run task %s (%s) ...' % (name, os.getpid())
        start = time.time()
        time.sleep(random.random() * 3)
        end = time.time()
        print 'task %s run %0.2f seconds ' % (name, (end - start))
if __name__ == '__main__':
        print 'parent process %s' % os.getpid()
        p = Pool()
        for i in range(5):
                p.apply_async(long_time_task, args=(i,))
        print 'waiting for all subprocesses done ...'
        p.close()
        p.join()
        print 'all subprocesses done'
