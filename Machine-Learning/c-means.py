# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:28:38 2019

@author: Thiag
"""

from sklearn import datasets
import numpy as np
from sklearn.metrics import confusion_matrix
import skfuzzy

iris = datasets.load_iris()

r = skfuzzy.cmeans(data = iris.data.T, c=3, m = 2, error = 0.005,
                   maxiter = 1000, init = None) #matrix transposta, c = grupos
#m = membershipt, criterio de parada
previsoes_porcentagem = r[1]

previsoes_porcentagem[0][0]

previsoes_porcentagem[1][0]

previsoes_porcentagem[2][0]

previsoes = previsoes_porcentagem.argmax(axis = 0)

resultados = confusion_matrix(iris.target,previsoes)