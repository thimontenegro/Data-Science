# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 20:49:47 2019

@author: Thiag
"""

#IMPORTS
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score

#Informacao do clima
clima = pd.read_csv('clima.csv',encoding = "ISO-8859-1")

#Variavel de previsores
previsores = clima.iloc[:,0:3].values

#Classe de busca
classe = clima.iloc[:,4].values

labelEncoder = LabelEncoder()

previsores[:,0] = labelEncoder.fit_transform(previsores[:,0])
previsores[:,1] = labelEncoder.fit_transform(previsores[:,1])
previsores[:,2] = labelEncoder.fit_transform(previsores[:,2])

X_treinamento,X_teste,y_treinamento,y_teste = train_test_split(
        previsores,classe, test_size = 0.3, random_state = 0)

naive_bayes = GaussianNB()
naive_bayes.fit(X_treinamento,y_treinamento)

#Criando previsoes
previsores = naive_bayes.predict(X_teste)
confusao = confusion_matrix(y_teste,previsores)

taxa_de_acerto = accuracy_score(y_teste,previsores)
taxa_de_erro = 1 - taxa_de_acerto

#Melhorar visualizacao
from yellowbrick.classifier import  ConfusionMatrix #visualizacao de modelos de Machine Learning
v = ConfusionMatrix(GaussianNB())
v.fit(X_treinamento,y_treinamento)
v.poof()