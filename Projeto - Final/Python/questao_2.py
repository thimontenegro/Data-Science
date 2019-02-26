# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:10:24 2019

@author: Thiag
"""

#Dados dois conjuntos de dados  {18,20,21,28,33,38,43,48,53,58,63} e 
#{871,1132,5435,1200,1356,1488,1600,2130,2454,3066,4090}, 
#calcule a correlação de Person
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


X = [18,20,21,28,33,38,43,48,53,58,63]
y = [871,1132,5435,1200,1356,1488,1600,2130,2454,3066,4090]
corr = np.corrcoef(X,y)


#Questão 29
#Dada a correlação r = 0,364454993
#desvio padrão de Y = 1354,17 e o desvio padrão de#
# X = 15,3348.
 #Calcule m = a inclinação da reta
X = 15.3348
Y = 1354.17
r = 0.364454993
m = r /(X/Y)

#Questão 30
m = 32.18395 #(inclinação), 

#Média de X = 38,54545 
X= 38.54545
#Média de Y = 2263,818
Y = 2263.818
#Interceptacao
b = Y - (m*X)
# 1041, 881, 1007, 895, 761, 1036, 1114, 980, 970, 1062,
#o desvio padrão e o terceiro quartil
dados = pd.Series([1041, 881, 1007, 895, 761, 1036, 1114, 980, 970, 1062])

dp = dados.std()
quartil = np.percentile(dados, 75)
#Questão 46
from scipy.stats import binom
#Binomial
#Se você jogar uma moeda 3 vezes, 
#qual a probabilidade de dar cara 1 vez?
prob_caras = binom.pmf(1,3,0.5)

#Questao 47
#Se eu passar 4 semáforos de dois tempos cada, 
#qual a probabilidade de pegar nenhum ou 4 semáforos abertos?
prob_sinal = binom.pmf(0,4,0.25) + binom.pmf(4,4,0.25)

#Você está fazendo esta prova de 100 questões.
# Supondo que de 6 questões, você não sabe a resposta e irá "chutar", 
#qual a probabilidade de você acertar três destas questões?

prob = binom.pmf(3,6,0.25) * 100
#49
#Em média, duas pessoas se infectam com um certo vírus por mês.
# Qual a probabilidade de, em um mês, 3 ou menos pessoas se infectarem?
from scipy.stats import poisson
poisson.pmf(3,2)
#50
poisson.cdf(3,2)

#52
from scipy.stats import norm
#Pergunta 52:
#Uma geladeira possui caixas de pescado, cujos pesos, em quilos, 
#estão normalmente distribuídos com média = 8 e desvio padrão igual a 4.
#Qual a chance de se tirar uma caixa pesando menos de 6 quilos?
media_caixa = 8
dp_caixa =4

prob_normal = norm.cdf(6,8,4)
#Qual a chance de se tirar uma caixa que tenha menos de 6 quilos ou 
#mais de 10 quilos?
prob_normal_mais_ou = prob_normal + norm.sf(10,8,4)

#59
#Você está pesquisando o gasto médio de seus funcionários c
#om viagens.#
# Foram pesquisadas 1000 Funcionários. O intervalo de confiança é de 95%. O gasto médio é de R$ 1.300.
# O desvio padrão é de R$ 300. 
#Calcule a margem de erro do seu estudo.
z = 1.96
media_gasto = 1.300
populacao = 1000
dp = 300
margem_erro = z * (dp/np.sqrt(populacao))

from scipy.stats import t

#Considerando a distribuição T de Student, 
#se a probabilidade é de 80%, o tamanho da amostra é de 4,
# qual é o valor de t?

t.cdf(0.05,0.8) 

#93
#1 - SABONETE, SABÃO, ESCOVA.
#2 - SABONETE, SABÃO, PASTA DE DENTE.
#3- SABONETE, SABÃO.
#4 - PASTA DE DENTE, ESCOVA.
#5 - PASTA DE DENTE, SABONETE.
from apyori import apriori

dados = pd.read_csv('transacoes.txt',header = None, encoding='utf8')

transacoes = []

for i in range(0,5):
    transacoes.append([str(dados.values[i,j]) for j in range(0,3)])
    
regras = apriori(transacoes,min_support = 0.5, min_confidence = 0.5)

resultados = list(regras)
resultados2 = [list(x) for x in resultados]

resultados3 = []
for j in range(0,4):
    resultados3.append([list(x) for x in resultados2[j][2]])
