# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:30:15 2019

@author: Thiag
"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from yellowbrick.classifier import ConfusionMatrix
from keras.models import Sequential  #Modelo Sequencial camadas de entrada e saida
from keras.layers import Dense #Rede Neural Densa
from keras.utils import np_utils

base = datasets.load_iris()


