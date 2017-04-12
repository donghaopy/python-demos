#!/usr/bin/python
#coding:utf8
'''
Created on 2017-4-12

@author: dh
'''
import re

html='''

</a>




<div class="thumb">

<a href="/article/118866930" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/11886/118866930/medium/app118866930.jpg" alt="知识改变命运" />
</a>

</div>

<div class="content">



<span>test001</span>


</div>

<div class="stats">
<span class="stats-vote"><i class="number">2503</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/118866930" data-share="/article/118866930" id="c-118866930" class="qiushi_comments" target="_blank">
<i class="number">37</i> 评论
</a>



</span>

<div class="content">



<span>test002</span>


</div>
</div>
'''
pattern = re.compile('<div\sclass="content">.*?</div>', re.S)
for item in re.findall(pattern, html):
    print '匹配实例:\r\n',item
    
    
    
    
    
    
    
    
    
