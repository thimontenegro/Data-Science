# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 01:17:06 2019

@author: Thiag
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
base = pd.read_csv('Eleicao.csv',sep=';')
plt.scatter(base.DESPESAS, base.SITUACAO)
base.describe()

#correlacao

np.corrcoef(base.DESPESAS, base.SITUACAO)

valoresInvestidos = base.iloc[:,2].values
valoresInvestidos = valoresInvestidos[:, np.newaxis]
situacao = base.iloc[:,1].values

modelo = LogisticRegression()
modelo.fit(valoresInvestidos, situacao)
modelo.coef_
modelo.intercept_

plt.scatter(valoresInvestidos, situacao)
valoresInvestidos_text = np.linspace(10, 3000)

def model(x):
    return 1 /(1 + np.exp(-x))

result = model(valoresInvestidos_text * modelo.coef_ + modelo.intercept_).ravel()
plt.plot(valoresInvestidos_text, result, color='red')

base_previsoes = pd.read_csv('NovosCandidatos.csv', sep = ';')

despesas = base_previsoes.iloc[:,1].values
despesas = despesas.reshape(-1,1)

previsoes_teste = modelo.predict(despesas)

base_previsoes = np.column_stack((base_previsoes,previsoes_teste))

(-0.89)**2
x = np.corrcoef([15,18,20,25,30,44])
