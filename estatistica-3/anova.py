# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 11:17:01 2019

@author: Thiag
"""

import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import MultiComparison

tratamento = pd.read_csv('anova.csv', sep= ';')
tratamento.boxplot(by = 'Remedio', grid=False)

modelo1 = ols('Horas ~ Remedio', data= tratamento).fit() #Variavel Resposta ~ Variavel Dependente
resultados1 = sm.stats.anova_lm(modelo1)

modelo2 = ols('Horas ~ Remedio * Sexo',data=tratamento).fit()
resultados2 = sm.stats.anova_lm(modelo2)


mc = MultiComparison(tratamento['Horas'], tratamento['Remedio'])
resultado_teste = mc.tukeyhsd()
print(resultado_teste)
resultado_teste.plot_simultaneous()