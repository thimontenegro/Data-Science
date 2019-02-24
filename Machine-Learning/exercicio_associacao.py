# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 20:52:37 2019

@author: Thiag
"""

import pandas as pd
from apyori import apriori

dados = pd.read_csv('exercicio.txt', header = None)
transacoes = []

for i in range(0,9):
   transacoes.append([str(dados.values[i,j]) for j in range(0,4)])

regras = apriori(transacoes,min_support = 0.5, min_confidence = 0.5)
resultados = list(regras)
resultados2 = [list(x) for x in resultados]

resultados3 = []
for j in range(0,7):
    resultados3.append([list(x) for x in resultados2[j][2]])