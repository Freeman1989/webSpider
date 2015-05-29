#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2

#创建一个密码管理者
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

#添加用户名和密码
top_level_url = "http://www.baidu.com"

#如果知道 realm，我们可以使用他代替”None“
password_mgr.add_password(None, top_level_url, 'why', '123')

#创建了一个新的handler
handler = urllib2.HTTPBasicAuthHandler(password_mgr)

#创建”opener“(OpenerDirector 实例)
opener = urllib2.build_opener(handler)

a_url = "http://www.baidu.com"

#使用opener获取一个URL
opener.open(a_url)

#安装opener
#现在所有调用 urllib2.urlopen 将用我们的opener.
urllib2.install_opener(opener)