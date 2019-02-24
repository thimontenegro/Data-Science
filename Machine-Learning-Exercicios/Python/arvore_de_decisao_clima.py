# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 22:44:49 2019

@author: Thiag
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier
import graphviz
from sklearn.tree import export_graphviz

clima = pd.read_csv('clima.csv',encoding = "ISO-8859-1")
previsores = clima.iloc[:,0:3].values
classe = clima.iloc[:,4].values

labelEncoder = LabelEncoder()

previsores[:,0] = labelEncoder.fit_transform(previsores[:,0])
previsores[:,1] = labelEncoder.fit_transform(previsores[:,1])
previsores[:,2] = labelEncoder.fit_transform(previsores[:,2])

X_treinamento,X_teste,y_treinamento,y_teste = train_test_split(previsores,
                                                               classe,
                                                               test_size= 0.3,
                                                               random_state = 0)

arvore = DecisionTreeClassifier()
arvore.fit(X_treinamento,y_treinamento)

export_graphviz(arvore, out_file='tree.dot')
previsoes = arvore.predict(X_teste)

tabela_confusao = confusion_matrix(previsoes,y_teste)

taxa_de_acerto = accuracy_score(y_teste,previsoes)

