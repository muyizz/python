# -*- coding: utf-8 -*-
# @Time : 2021/3/10 22:47
# @Author : yangyong
# @File : 输入输出函数.py
#
name=1
'''
input函数
功能： 接受标准的输入数据（即从键盘输入），返回为string类型（字符串）
语法格式： input([prompt])
     1,prompt是一个可选参数，给用户提示信息； 不传该参数，则没有提示信息，用户直接从键盘输入数据
     2，本课程规定，如果一个参数写在一对方括号‘[...]’中，则表示该参数是可选参数
'''
#示例
name = input('输入你的姓名：')
print(name)

'''
eval函数
功能：计算字符串对应的表达式，返回表达式的计算结果
语法格式：eval（expression）
     1,expression 是字符串类型的参数，对应一个有效的python表达式
     2,eval函数的完整语法格式为：eval(expression),globals=None,locals=None)
'''
#示例
r=eval(input('请输入与一个有效的表达式:'))
g=eval('5*8')
print(r,g)

'''
print函数
功能:将各种类型的数据(字符串,整数,浮点数,列表,字典等)输出到屏幕上
语法格式:print(object)
'''
#示例
print('helloword')
print(10)
print(3.5)
print([1,3,5,'list'])
print({1:'A',2:'B',3:'C',4:'D'})