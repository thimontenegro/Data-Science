# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 03:38:18 2019

@author: Thiag
"""

import numpy as np
import pandas as pd
from math import ceil

populacao = 150
amostra = 15
k =ceil(populacao / amostra)

random = np.random.randint(low = 1, high = k + 1, size = 1)

acumulador = random[0]
sorteados = []

for i in range(amostra):
    sorteados.append(acumulador)
    acumulador += k

iris = pd.read_csv('iris.csv')

base_final = iris.loc[sorteados]


    