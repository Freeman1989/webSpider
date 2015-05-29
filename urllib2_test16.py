#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2

my_url = 'http://www.goole.cn'
response = urllib2.urlopen(my_url)
redirected = response.geturl() == my_url
print redirected

my_url = 'http://rrurl.cn/b1UZuP'
response = urllib2.urlopen(my_url)
redirected = response.geturl() == my_url
print redirected