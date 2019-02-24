# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 11:27:48 2019

@author: Thiag
"""

from sklearn import datasets
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#Criando base de dados
iris = datasets.load_iris()
unicos,quantidade = np.unique(iris.target, return_counts = True)
#Separa os grupos e divide em 3 grupos diferentes

cluster = KMeans(n_clusters = 3) #quantos cluster que definir
cluster.fit(iris.data)

centroides = cluster.cluster_centers_ #centroides e centros de cada 1
previsoes = cluster.labels_

unicos2,quantidade2 = np.unique(previsoes, return_counts = True)
resultados = confusion_matrix(iris.target,previsoes)

plt.scatter(iris.data[previsoes == 0, 0],
            iris.data[previsoes==0,1],
            c='blue',label='Virgica')

plt.scatter(iris.data[previsoes == 1, 0],
            iris.data[previsoes==1,1],
            c='red',label='Versicolor')

plt.scatter(iris.data[previsoes == 2, 0],
            iris.data[previsoes==2,1],
            c='green',label='Setosa')
plt.legend()