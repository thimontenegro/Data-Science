# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 18:15:03 2019

@author: Thiag
"""

from sklearn import datasets
from sklearn.metrics import confusion_matrix
import numpy as np
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster import cluster_visualizer #visualizacao

iris = datasets.load_iris()

cluster = kmedoids(iris.data[:,0:2],[3,12,20])
cluster.get_medoids()
cluster.process() #processamento
previsoes = cluster.get_clusters()
medoides = cluster.get_medoids() #gera os medoides, pontos mais representativos

visualizacao = cluster_visualizer()
visualizacao.append_clusters(previsoes,iris.data[:,0:2])
visualizacao.append_cluster(medoides, data=iris.data[:,0:2], marker = '*',markersize=15)
visualizacao.show()

lista_previsoes = []
lista_real = []
for i in range(len(previsoes)):
    for j in range(len(previsoes[i])):
        lista_previsoes.append(i)
        lista_real.append(iris.target[previsoes[i][j]])
        
list_previsoes = np.asarray(lista_previsoes) #mudanca para o tipo numpy
lista_real = np.asarray(lista_real)
resultados = confusion_matrix(lista_real,lista_previsoes)