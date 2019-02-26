# -*- coding: utf-8 -*-
#UTF-8
"""
Created on Tue Feb 26 00:49:02 2019

@author: Thiag
"""

"""
"Nossa taxa de inadimplência é de 35%. 
Você acha que com o uso das suas técnicas, 
conseguimos baixar este índice para pelo menos, 25%?"

Crie um modelos de machine learning 
e tente chegar a um índice de inadimplência
 aproximado, de 25%.

Você pode fazer em R ou Python.

Descreva algoritmos e técnicas utilizadas
, bem como o índice alcançado.
"""
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.tree import DecisionTreeClassifier
import graphviz
from sklearn.tree import export_graphviz

base = pd.read_csv("Credito.csv",sep=';', encoding="ISO-8859-1")

previsores = base.iloc[:,0:19].values
classe = base.iloc[:,19].values

labelEncoder = LabelEncoder()

previsores[:,0] = labelEncoder.fit_transform(previsores[:,0])
previsores[:,2] = labelEncoder.fit_transform(previsores[:,2])
previsores[:,3] = labelEncoder.fit_transform(previsores[:,3])
previsores[:,5] = labelEncoder.fit_transform(previsores[:,5])
previsores[:,6] = labelEncoder.fit_transform(previsores[:,6])
previsores[:,7] = labelEncoder.fit_transform(previsores[:,7])
previsores[:,8] = labelEncoder.fit_transform(previsores[:,8])
previsores[:,9] = labelEncoder.fit_transform(previsores[:,10])
previsores[:,11] = labelEncoder.fit_transform(previsores[:,11])
previsores[:,13] = labelEncoder.fit_transform(previsores[:,13])
previsores[:,14] = labelEncoder.fit_transform(previsores[:,14])
previsores[:,16] = labelEncoder.fit_transform(previsores[:,16])
previsores[:,18] = labelEncoder.fit_transform(previsores[:,18])


X_treinamento, x_teste, y_treinamento,y_teste = train_test_split(
        previsores,classe,test_size = 0.5,random_state = 0)
X_treinamento.reshape(-1,1)
arvore = DecisionTreeClassifier()
arvore.fit(X_treinamento,y_treinamento)

previsoes = arvore.predict(x_teste)
confusao = confusion_matrix(y_teste,previsoes)
taxa_acerto  = accuracy_score(y_teste,previsoes)
taxa_de_erro = 1 - taxa_acerto
"""
Como queremos 75% de acertos e ataxa do nosso algoritomo é de 68%
logo a arvore de decisao é invalida
"""