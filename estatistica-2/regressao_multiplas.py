# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 00:14:47 2019

@author: Thiag
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot
import statsmodels.formula.api as sm #modelos do r no python
base = pd.read_csv('mt_cars.csv')

base = base.drop(['Unnamed: 0'], axis =1)

X = base.iloc[:,2].values
y = base.iloc[:,0].values
correlacao = np.corrcoef(X,y)
X = X.reshape(-1,1)

modelo = LinearRegression()
modelo.fit(X,y)
modelo.intercept_
modelo.coef_

#visualizacao do R^2
modelo.score(X,y)

previsoes = modelo.predict(X)
modelo_ajustado = sm.ols(formula = 'mpg ~ disp', data=base)
modelo_treinado = modelo_ajustado.fit()
modelo_treinado.summary()

plt.scatter(X,y)
plt.plot(X, previsoes, color = 'red')

X1 = base.iloc[:,1:4].values
y1 = base.iloc[:,0].values
modelo2 = LinearRegression()
modelo2.fit(X1,y1)

modelo2.score(X1, y1)
modelo2_ajustado = sm.ols(formula = 'mpg ~ cyl + disp + hp', data=base)
modelo2_treinado = modelo_ajustado.fit()
modelo2_treinado.summary()

novo = np.array([4,200,100])
novo = novo.reshape(1,-1)
modelo.predict(novo)