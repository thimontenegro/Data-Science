# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 19:44:50 2019

@author: Thiag
"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from scipy import stats
from sklearn import datasets

iris = datasets.load_iris()
stats.describe(iris.data) #valores referentes ao data da iris

#Pegar os valaores 
previsores = iris.data
#Objeto da classe em si
classe = iris.target
#Criar as instancias de treinamento e teste
X_treinamento,X_teste,y_treinamento,y_teste = train_test_split(
        previsores,classe, test_size = 0.3,random_state = 0)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_treinamento,y_treinamento)
#Criando previsoes
previsoes = knn.predict(X_teste)
#Menor distancia no mapeando do treinamento de dados
#vai ser classificado em alguma de suas instancias
tabela_confusao = confusion_matrix(y_teste,previsoes)
taxa_de_acertos = accuracy_score(y_teste,previsoes)
taxa_de_erros =  1 - taxa_de_acertos