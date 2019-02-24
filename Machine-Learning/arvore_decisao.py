# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 17:56:44 2019

@author: Thiag
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.tree import DecisionTreeClassifier
import graphviz
from sklearn.tree import export_graphviz

credito = pd.read_csv('Credit.csv')
previsores = credito.iloc[:,0:20].values
classe = credito.iloc[:,20].values

labelEncoder = LabelEncoder()
#LabelEncoder realiza a transformacao de dados categoricos p/ numericos
previsores[:,0] = labelEncoder.fit_transform(previsores[:,0])
previsores[:,2] = labelEncoder.fit_transform(previsores[:,2])
previsores[:,3] = labelEncoder.fit_transform(previsores[:,3])
previsores[:,5] = labelEncoder.fit_transform(previsores[:,5])
previsores[:,6] = labelEncoder.fit_transform(previsores[:,6])
previsores[:,8] = labelEncoder.fit_transform(previsores[:,8])
previsores[:,9] = labelEncoder.fit_transform(previsores[:,9])
previsores[:,11] = labelEncoder.fit_transform(previsores[:,11])
previsores[:,13] = labelEncoder.fit_transform(previsores[:,13])
previsores[:,14] = labelEncoder.fit_transform(previsores[:,14])
previsores[:,16] = labelEncoder.fit_transform(previsores[:,16])
previsores[:,18] = labelEncoder.fit_transform(previsores[:,18])
previsores[:,19] = labelEncoder.fit_transform(previsores[:,19])

X_treinamento,X_teste,y_treinamento,y_teste = train_test_split(previsores,
                                                               classe,
                                                               test_size = 0.3,
                                                               random_state = 0)

arvore = DecisionTreeClassifier()
arvore.fit(X_treinamento,y_treinamento) #Conjunto de Treinamento, Respostas do Treinamento

export_graphviz(arvore,out_file = 'tree.dot')  #Visualizacao da Arvore
previsoes = arvore.predict(X_teste) #Validacao da Classificacao do modelo
confusao = confusion_matrix(y_teste,previsoes)

taxa_acerto = accuracy_score(y_teste,previsoes) #Passa o valores corretos e os dados da nova arvore
taxa_erro = 1 - taxa_acerto