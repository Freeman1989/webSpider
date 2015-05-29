#!/usr/bin/pythrn
# -*- coding: utf-8 -*-

from urllib2 import urlopen, URLError, HTTPError

old_url = 'http://rrurl.cn/b1UZuP'
response = urlopen(old_url)
print 'Old url: ' + old_url
print 'Real url: ' + response.geturl()
