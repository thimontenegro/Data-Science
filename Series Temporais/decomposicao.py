# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 17:56:17 2019

@author: Thiag
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from statsmodels.tsa.seasonal import seasonal_decompose

base = pd.read_csv('AirPassengers.csv')
dateparse = lambda dates: pd.datetime.strptime(dates,'%Y-%m')
base = pd.read_csv('AirPassengers.csv', parse_dates = ['Month'],
                   index_col = 'Month', date_parser = dateparse)
ts = base['#Passengers']
plt.plot(ts)          


decomposicao = seasonal_decompose(ts)

tendencia = decomposicao.trend

sazonal = decomposicao.seasonal

aleatorio = decomposicao.resid

plt.plot(sazonal)
plt.plot(tendencia)
plt.plot(aleatorio)

plt.subplot(4,1,1)
plt.plot(ts, label ='Original')
plt.legend(loc = 'best')

plt.subplot(4,1,2)
plt.plot(tendencia, label ='Tendência')
plt.legend(loc = 'best')

plt.subplot(4,1,3)
plt.plot(sazonal, label ='Sazonalidade')
plt.legend(loc = 'upper left')

plt.subplot(4,1,4)
plt.plot(aleatorio, label ='Elemento Aleatorio')
plt.legend(loc = 'upper left')
plt.tight_layout()