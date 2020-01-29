# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 21:31:51 2019

@author: marco
"""

import math

v1 = [0]
v2 = [0.5, 4.5, 9.6, 3.4]

def dist_euclidiana(v1, v2):
	dim, soma = len(v1), 0
	for i in range(dim):
		soma += math.pow(v1[i] - v2[i], 2)
	return math.sqrt(soma)

print('%.2f' % dist_euclidiana(v1, v2))