#!/usr/bin/pythrn
# -*- coding: utf-8 -*-

from urllib2 import urlopen, URLError, HTTPError

old_url = 'http://www.baidu.com'
response = urlopen(old_url)
print 'Info():'
print response.info()