# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 22:45:06 2019

@author: Thiago Montenegro
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier
credito = pd.read_csv('Credito.csv',sep=';',encoding='ISO-8859-1')

previsores = credito.iloc[:,0:19].values
classe = credito.iloc[:,19].values
#Enconder => Transformar dados categoricos em valores números
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


#Divisao de dados
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores,classe,test_size = 0.3, random_state = 0)
#Criacao do modelo da floresta, com 1000 arvores
floresta = RandomForestClassifier(n_estimators = 1000) 
#Realiza o treinamento do modelo da floresta
floresta.fit(X_treinamento,y_treinamento)
#Previsoes
previsoes = floresta.predict(X_teste)
confusao = confusion_matrix(y_teste,previsoes)
#Taxa de acertos
taxa_de_acerto = accuracy_score(y_teste,previsoes)
taxa_de_erro = 1 - taxa_de_acerto