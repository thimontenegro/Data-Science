# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 09:55:43 2019

@author: Thiag
"""

from scipy.stats import poisson
#3 acidentes por dia sabendo que a media é de 2 acidentes
poisson.pmf(3,2)

#3 ou menos acidentes
poisson.cdf(3,2)
#3 ou mais
poisson.sf(3,2)
poisson.pmf(12,10)