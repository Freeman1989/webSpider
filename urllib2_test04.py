#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2

url = "http://www.imooc.com"

user_agent = "Mozilla/4.0 (compatible; MSIE5.5; Windows NT)"
values = {'name' : 'WHY',
         'location' : 'SDU',
         'language' : 'Python' }

headers = { 'User-Agent' : user_agent }
data = urllib.urlencode(values) #编码工作
req = urllib2.Request(url, data, headers) #发送请求同时传data表单
response = urllib2.urlopen(req) #接受反馈的信息
the_page = response.read() #读取反馈的内容
print the_page
