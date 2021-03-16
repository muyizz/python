# -*- coding: utf-8 -*-
# @Time : 2021/3/10 22:37
# @Author : yangyong
# @File : helloword.py
print("你好，世界")#中文需要设定UTF-8编码格式
print('helloword') #在屏幕上输出helloword

'''
此处是多行注释
'''
#此处是单行注释】

'''
python语言通过代码缩进方式体现各条语句之间的逻辑关系

对于同一层次的代码，必须使用相同的缩进方式，否则会报错
'''
bPrint = True
if bPrint:
    bPrint = False
    print('Yes')
print(bPrint)