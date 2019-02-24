# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 16:49:32 2019

@author: Thiag
"""

import pandas as pd
from sklearn.model_selection import train_test_split #dividir entre treino e teste
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score #tabela d confusao, e saber os dados
credito = pd.read_csv('Credit.csv') #carrega os dados

#variavel de previsores
previsores = credito.iloc[:,0:20].values #1 argumento pega todas as linhas
#e as colunas de 0 - 19 ou da 1-19 exceto a de classe!

classe = credito.iloc[:,20].values #pega a classe de identificacao

#GaussianNB nao trabalha com dados categoricos!
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


X_treinamento,X_teste, y_treinamento, y_teste = train_test_split(
        previsores,classe,test_size = 0.3, random_state = 0)
#passa os dados de atributos no 1 argumento
#2 a classe com quem queremos realizar a identificacao
#o tamanho da nossa base de testes que é 30% e 70% treino
#random_state dividir a base de forma igual


naive_bayes = GaussianNB()
naive_bayes.fit(X_treinamento, y_treinamento) #pra cada valores em X tenho a resposta em Y


#Criando previsoes

previsoes = naive_bayes.predict(X_teste) #predict passando os dados de teste!

confusao = confusion_matrix(y_teste,previsoes) #comparar os resultados do treino com as previsoes

taxa_acerto = accuracy_score(y_teste,previsoes)

taxa_erro = 1 - taxa_acerto

#Visualizacaoes
from yellowbrick.classifier import  ConfusionMatrix #visualizacao de modelos de Machine Learning
v = ConfusionMatrix(GaussianNB()) #Tabela Confusao
#treinamento
v.fit(X_treinamento, y_treinamento) #treinamento
v.score(X_teste,y_teste)  #Calculo do Erro
v.poof() #Visualizar


#SIMULACAOOOOO COM NOVOS REGISTROS!
novo_cliente = pd.read_csv('NovoCredit.csv')
novo_cliente = novo_cliente.iloc[:,0:20].values #deixar de forma de numpy array

novo_cliente[:,0] = labelEncoder.fit_transform(novo_cliente[:,0])
novo_cliente[:,2] = labelEncoder.fit_transform(novo_cliente[:,2])
novo_cliente[:,3] = labelEncoder.fit_transform(novo_cliente[:,3])
novo_cliente[:,5] = labelEncoder.fit_transform(novo_cliente[:,5])
novo_cliente[:,6] = labelEncoder.fit_transform(novo_cliente[:,6])
novo_cliente[:,8] = labelEncoder.fit_transform(novo_cliente[:,8])
novo_cliente[:,9] = labelEncoder.fit_transform(novo_cliente[:,9])
novo_cliente[:,11] = labelEncoder.fit_transform(novo_cliente[:,11])
novo_cliente[:,13] = labelEncoder.fit_transform(novo_cliente[:,13])
novo_cliente[:,14] = labelEncoder.fit_transform(novo_cliente[:,14])
novo_cliente[:,16] = labelEncoder.fit_transform(novo_cliente[:,16])
novo_cliente[:,18] = labelEncoder.fit_transform(novo_cliente[:,18])
novo_cliente[:,19] = labelEncoder.fit_transform(novo_cliente[:,19])


naive_bayes.predict(novo_cliente)
