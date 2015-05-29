#!/usr/bin/python
#  -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html)
print soup.prettify()

#Tag
print soup.title
print soup.head
print soup.a
print soup.p

print type(soup.a)

print soup.name
print soup.head.name

print soup.p.attrs
print soup.p['class']
print soup.p.get('class')
soup.p['class']="newClass"
print soup.p
del soup.p['class']
print soup.p

#NavigableString
print soup.p.string
print type(soup.p.string)

#BeautifulSoup
print type(soup.name)
print soup.name
print soup.attrs

#Comment
print soup.a
print soup.a.string
print type(soup.a.string)

if type(soup.a.string)=='bs4.element.Comment':
    print soup.a.string

#遍历文档树
#直接子节点
print soup.head.contents
print soup.head.contents[0]

print soup.head.children
for child in soup.body.children:
    print child

#所有子孙节点
for child in soup.descendants:
    print child

#节点内容
print soup.head.string
print soup.title.string
print soup.html.string

#多个内容
for string in soup.strings:
    print(repr(string))

for string in soup.stripped_strings:
    print(repr(string))

#父节点
p = soup.p
print p.parent.name
content = soup.head.title.string
print content.parent.name

#全部父节点
content = soup.head.title.string
for parent in content.parents:
    print parent.name

#兄弟节点
print soup.p.next_sibling
print soup.p.prev_sibling
print soup.p.next_sibling.next_sibling

