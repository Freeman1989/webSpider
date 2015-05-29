#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2

enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http": 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')

url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {"username": "xianglijiang@gmail.com", "password": "xxxxxxxx"}
headers = {'User-Agent': user_agent,
            'Referer': 'http://www.zhihu.com/articles' }
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
request.get_method = lamdba: 'PUT' # or 'DELETE'
response = urllib2.urlopen(request)
print response.read()
