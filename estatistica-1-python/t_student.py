# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 15:33:57 2019

@author: Thiag
"""

from scipy.stats import t
# > #media 75 amostra 9 dp 10 
#> #qual a prob < 80
t.cdf(1.5, 8)
#maior que 80
t.sf(1.5,8)
t.sf(1.5,8) +  t.cdf(1.5,8)