# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 19:43:58 2019

@author: Thiag
"""

import pandas as pd
import matplotlib.pylab as plot
from statsmodels.tsa.arima_model import ARIMA
from pyramid.arima import auto_arima
base = pd.read_csv('AirPassengers.csv')
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
base = pd.read_csv('AirPassengers.csv',parse_dates=['Month'],
                   index_col = 'Month', date_parser = dateparse)
ts = base['#Passengers']

plot.plot(ts)        
#arima p = no de termos auto-regressivos, q=media da mediamovel, d = diferenca
modelo = ARIMA(ts,order =(2,1,2))
modelo_treinado = modelo.fit()
modelo_treinado.summary()

previsoes = modelo_treinado.forecast(steps = 12)[0]

eixo = ts.plot()
modelo_treinado.plot_predict('1960-01-01','1970-01-01'
                             , ax = eixo, plot_insample = False)


#pyramid
modelo_auto = auto_arima(ts, m=12, seasonal = True, trace = True)
modelo_auto.summary()
proximos_12 = modelo_auto.predict(n_periods = 12)