# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import pack_1.change as change
from pandas_datareader import data
gatafga={'谷歌':'GOOG','亚马逊':'AMZN','Facebook':'FB','苹果':'APPLE','阿里巴巴':'AL'}
start_date = '2019-01-01'
end_date = '2020-02-11'
babaDf = data.get_data_yahoo(gatafga['阿里巴巴'],start_date,end_date)
#closeCol = babaDf['Close']
#babaChange = change(closeCol)
"""趋势图"""
##print(babaDf)
#babaDf.index
#babaDf.plot(y='Close')
#plt.xlabel('时间')
#plt.ylabel('股价（美元）')
#plt.title('2019年阿里巴巴股价走势')
'''柱状图'''
"""
googleDf =data.get_data_yahoo(gatafga['谷歌'],start_date,end_date)
closeCol = googleDf['Close']
googleChange = change(closeCol)

amazDf = data.get_data_yahoo(gatafga['亚马逊'],start_date,end_date)
closeCol = amazDf['Close']
amazChange = change(closeCol)

facebookDf = data.get_data_yahoo(gatafga['Facebook'],start_date,end_date)
closeCol = facebookDf['Close']
facebookChange = change(closeCol)

ax1 = googleDf.plot(y='Close',lable = 'google')
amazDf.plot(ax=ax1,y='Close',lable = 'amaz')
facebookDf.plot(ax= ax1,y='Close',lable = 'facebook')"""

gafataMenList = [babaDf['Close'].mean()]
gafataMenSer = pd.Series(gafataMenList,index=['阿里巴巴']).sort_values(ascending=False)
gafataMenSer.plot(kind = 'bar',label ='GAFATA')


plt.xlabel('company')
plt.ylabel('股价（美元）')
plt.title('2019年至今股价累计涨幅')
plt.grid(False)
plt.show()