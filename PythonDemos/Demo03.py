#! /usr/bin/env python
#_*_coding:utf-8 _*_
'''
Created on 2017-3-9

@author: dh
'''
#定义函数
def my_abs(x):
    if x>=0:
        return x
    else:
        #print('-x的值是%d %',-x)
        return -x
#调用函数
value=raw_input("please enter your number:")
value=int(value)
print(my_abs(value))

#可变参数、默认参数
####默认参数必须指向不变对象####
def encroll(name,gender,age=5,city='BeiJing'):
    print 'name:',name
    print 'gender:',gender
    print 'age:',age
    print 'city:',city
#使用默认参数
encroll('test', 'boy')
#赋值给默认参数
encroll('test', 'boy',6)
#指定哪个默认参数
encroll('test', 'boy',city='ShangHai')

#使用可变参数 *tuple
def calc(*args):
    sum=0;
    for arg in args:
        sum+=arg*arg
    return sum
print(calc(1,2,3))

#使用关键字参数 **kw
def person(name,age,**kw):
    print 'name',name
    print 'age',age
    print 'dic',kw

person('test',1,height='170',weight='62')
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')



















