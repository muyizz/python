# -*- coding: utf-8 -*-
# @Time : 2020/9/5 14:26
# @Author : yangyong
# @File : change.py
def change(column):
    buyPrice = column[0]
    curPrice = column[column.siez-1]
    priceChange = (curPrice - buyPrice)/buyPrice
    if (priceChange>0):
        print('股价累计上涨=',priceChange*100,'%')
    elif(priceChange ==0):
        print('股票没有变化',priceChange*100,'%')
    else:
        print('股票累计下跌',priceChange*100,'%')
    return priceChange
