# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 02:37:06 2019

@author: Thiag
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot

base = pd.read_csv('cars.csv')
base = base.drop(['Unnamed: 0'], axis = 1)

X = base.iloc[:, 1].values #velocidades
X = X.reshape(-1,1)
y = base.iloc[:,0].values # variavel dependente
corr = np.corrcoef(X,y) #correlacao forte

modelo = LinearRegression()
#treinamento
modelo.fit(X,y)

modelo.intercept_
modelo.coef_

plt.scatter(X,y)
plt.plot(X, modelo.predict(X), color='purple')
#distancia de parada 22 pés
modelo.intercept_ + modelo.coef_ * 22

modelo._residues #residuos distancia dos pontos a linha
visualizador = ResidualsPlot(modelo)
visualizador.fit(X,y)
visualizador.poof()

