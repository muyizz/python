# -*- coding: utf-8 -*-
# @Time : 2021/3/10 22:34
# @Author : yangyong
# @File : 简单的爬虫.py
from urllib import request
url = 'https://www.icourse163.org/'
content = request.urlopen(url).read()
print(content)