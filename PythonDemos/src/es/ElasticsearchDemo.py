#!/usr/local/env python
# coding:utf-8
"""
Created on 2017-4-12
elasticsearch检索
相比solr：
            轻量级：安装启动方便，下载文件之后一条命令就可以启动；
    Schema free：可以向服务器提交任意结构的JSON对象，Solr中使用schema.xml指定了索引结构；
            多索引文件支持：使用不同的index参数就能创建另一个索引文件，Solr中需要另行配置；
            分布式：Solr Cloud的配置比较复杂；
            写入速度：ES是REST API，这点上没有Solr的Binary写入快速
@author: dh
"""
# @staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样
# @classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数
import elasticsearch
import unittest
import traceback
import time
class ES(object):
    @classmethod
    def connect_host(cls):
        hosts = [{"host":"192.168.10.211"}, {"host":"192.168.10.212"},
              {"host":"192.168.10.213"}, {"host":"192.168.10.214"},
              {"host":"192.168.10.215"}, {"host":"192.168.10.216"}
        ]
        try:
            es = elasticsearch.Elasticsearch(
               hosts,
               #sniff_on_start=True,
               sniff_on_connection_fail=True,
               sniffer_timeout=600
            )
            return es
        except Exception as ex:
            print '异常信息:',str(ex)
            print traceback.print_exc()


import uuid
class ESTest(unittest.TestCase):
    #连接es集群
    def setUp(self):
        global es
        es = ES.connect_host()
        self.assertTrue(es)
    def test_es(self):
        #id查询
        self.assertTrue(es.exists('cluestore2', 'info', '4028b8815b4111bc015b4113b0d80001'))
    
    #插入单个document
    def test_create(self):
        #print len(str(uuid.uuid4()))
        id=str(uuid.uuid4())
        es.create('cluestore2', 'info', id, {'clueId':id,'clueName':'python插入','clueSource':'测试'});
    
    #测试搜索
    def test_search(self):    
        body={
            "query": {
                "filtered": {
                    "query": {"matchAll": {}},
                }
            }
        }
        results=es.search('cluestore2', 'info', body)
        #字典中的list
        for result in results['hits']['hits']:
            #直接输出中文
            return result['_source']['clueName']
    #批量插入bulk
    #bulk暂时有问题
    def test_bulk(self):
        body=[]
        i=0
        while i<5:
            obj={
               "_index": "cluestore2",
               "_type": "info",
               "_id": str(uuid.uuid4()),
               "_source": {
                    'clueName':'测试'+str(i),
                    'clueSource':'来源'+str(i),
                    'createDate':int(time.time())
                }
            }  
            body.append(obj)
            i+=1
        #print body
        es.bulk(body,'cluestore2', 'info')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    