# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 22:41:02 2019

@author: Thiag
"""

from scipy.stats import norm
#Conjunto de objetos de uma cesta, media 9 e o dp  e´2
#probabilidade de tirar um objeto de pesor menor que 6
#menor = cdf
norm.cdf(6,8,2)
#peso maior que 6
norm.sf(6,8,2)
1 - norm.cdf(6,8,2)
#pesor menor que do 6 e maior que 10
norm.cdf(6,8,2) + norm.sf(10,8,2)

#pesor menor do que 10 e maior uqe 8
norm.cdf(10,8,2) - norm.sf(8,8,2)

###############TESTES NORMALL####n#########

norm.cdf(1500,1250,480)