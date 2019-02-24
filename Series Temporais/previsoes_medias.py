# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 19:19:25 2019

@author: Thiag
"""

import pandas as pd
import matplotlib.pylab as plot

base = pd.read_csv('AirPassengers.csv')
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
base = pd.read_csv('AirPassengers.csv',parse_dates=['Month'],
                   index_col = 'Month', date_parser = dateparse)
ts = base['#Passengers']

plot.plot(ts)          


#Previsoes p/ o futuro e extrapolar os dados

ts.mean() #Previsao por media é errado

ts['1960-01-01':'1960-12-01'].mean() #476.1667

#media movel utiliza a media de 12 datas antes do dia que queremos prever

media_movel = ts.rolling(window = 12).mean()
ts[0:12].mean()
ts[1:13].mean()

plot.plot(ts) #serie temporal
plot.plot(media_movel,color='red')

previsoes = []
for i in range(1,13):
    superior = len(media_movel) - i
    inferior = superior - 11
    #print(inferior)
    #print(superior)
    #print('---')
    previsoes.append(media_movel[inferior:superior].mean())
    
previsoes = previsoes[::-1]    
plot.plot(previsoes)