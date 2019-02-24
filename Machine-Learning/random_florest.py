# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 19:55:37 2019

@author: Thiag
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier
#Divisao de Classe e Os Previsores
credito = pd.read_csv('Credit.csv')
previsores = credito.iloc[:,0:20].values
classe = credito.iloc[:,20].values

#Trasnformacao dos dados quanlitativos em quantitaivos
labelEncoder = LabelEncoder()

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

#Divisao de Dados de Treinamento e teste
X_treinamento,X_teste,y_treinamento,y_teste = train_test_split(previsores,
                                                               classe,
                                                               test_size = 0.3,random_state = 0)

#Realizacao do treinamento                                   random_state = 0)
floresta = RandomForestClassifier(n_estimators = 1000) #cria 100 arvores de decisao
floresta.fit(X_treinamento,y_treinamento)
previsoes = floresta.predict(X_teste) #armazena as respostas finais
#Submente os dados do X_teste ao 100 florestas
#e o resultado final vai decidir sobre o conjunto de treinamento
confusao = confusion_matrix(y_teste,previsoes)

#taxas de acertos
taxa_de_acertos = accuracy_score(y_teste,previsoes)


floresta.estimators_