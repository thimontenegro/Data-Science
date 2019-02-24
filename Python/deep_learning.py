# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 06:20:51 2019

@author: Thiag
"""
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import np_utils
import numpy as np
from sklearn.metrics import confusion_matrix
from keras.datasets import mnist
#Carregamento de dados especifico do conjunto
(X_treinamento, y_treinamento),(X_teste, y_teste) = mnist.load_data()
plt.imshow(X_treinamento[2], cmap='gray')
plt.title(y_treinamento[2])

#Modelando os conjuntos
X_treinamento = X_treinamento.reshape((len(X_treinamento),np.prod(X_treinamento.shape[1:])))
X_teste = X_teste.reshape((len(X_teste), np.prod(X_teste.shape[1:])))
#Normalizando dados entre 0 - 1
X_treinamento = X_treinamento.astype('float32')
X_teste = X_teste.astype('float32')

X_treinamento /= 255
X_teste /= 255

y_treinamento = np_utils.to_categorical(y_treinamento,10) #Saida do neuronio 10
y_teste = np_utils.to_categorical(y_teste,10)

modelo = Sequential()
modelo.add(Dense(units = 64, activation = 'relu',input_dim = 784))
#64 neuronios e funcao ativacao relu > 1, retorna o valor
#neuronios de entrada é = ao numero de atributos
modelo.add(Dropout(0.2)) #zerar o numero dos neuronios
modelo.add(Dense(units = 64, activation ='relu'))
modelo.add(Dropout(0.2))
modelo.add(Dense(units = 64, activation ='relu'))
modelo.add(Dropout(0.2))
modelo.add(Dense(units = 64, activation ='relu'))
modelo.add(Dropout(0.2))
modelo.add(Dense(units = 10, activation='softmax')) #probabilidade de cada uma das letras
modelo.summary()
modelo.compile(optimizer = 'adam', loss = 'categorical_crossentropy',
               metrics = ['accuracy'])
historico = modelo.fit(X_treinamento,y_treinamento,epochs = 20, validation_data = (X_teste,y_teste))
historico.history.keys()
plt.plot(historico.history['val_loss'])
plt.plot(historico.history['val_acc'])
previsoes = modelo.predict(X_teste)
y_teste_matrix = [np.argmax(t) for t in y_teste]
y_previsoes_matrix = [np.argmax(t) for t in previsoes]

confusao = confusion_matrix(y_teste_matrix,y_previsoes_matrix)

y_treinamento[20]
novo = X_treinamento[20]
novo = np.expand_dims(novo, axis = 0)
pred = modelo.predict(novo)
