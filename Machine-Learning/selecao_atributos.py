# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 18:39:28 2019

@author: Thiag
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.svm import SVC
from sklearn.ensemble import ExtraTreesClassifier #Importancia dos Atributos
credito = pd.read_csv('Credit.csv')
previsores = credito.iloc[:,0:20].values
classe = credito.iloc[:,20].values

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

X_treinamento,X_teste,y_treinamento,y_teste = train_test_split(previsores,
                                                               classe,
                                                               test_size = 0.3,
#Realizacao do treinamento                                            random_state = 0)
svm = SVC()
svm.fit(X_treinamento,y_treinamento)
previsoes = svm.predict(X_teste)
taxa_acerto = accuracy_score(y_teste, previsoes) #igual a naive bayes
#Random Florest
forest = ExtraTreesClassifier()
#Realiza o treinamento dos dados
forest.fit(X_treinamento, y_treinamento)

importancias = forest.feature_importances_

X_treinamento2 = X_treinamento[:,[0,1,2,3]]
X_teste2 = X_teste[:,[0,1,2,3]]

svm2 = SVC()
svm2.fit(X_treinamento2, y_treinamento)

novas_previsoes = svm2.predict(X_teste2)

taxa_acerto = accuracy_score(y_teste,novas_previsoes)