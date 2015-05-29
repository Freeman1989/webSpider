#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2

values = {"username":"xianglijiang@gmail.com","password":"xxxxxxxx"}
#values = {}
#values['username'] = "xianglijiang@gmail.com"
#values['password'] = "xxxxxxxx"
data = urllib.urlencode(values)
url = "http://www.imooc.com/user/logout"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()
