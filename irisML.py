# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:17:49 2019

@author: marco

"""


import matplotlib.pyplot as plt
import pandas as table
import numpy as np

from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
digits = datasets.load_digits()

#digits.data é a base de dados e target é a classe


clf = svm.SVC(gamma=0.001,C=100.)
clf.fit(digits.data[:-1], digits.target[:-1])
clf.predict(digits.data[-1:])

#decision_function_shape='ovr', degree=3, gamma=0.001, kernel


treino = int(np.floor(len(digits.data)*0.7))

teste = int(np.floor(len(digits.data)*0.3))

clf.fit(digits.data[:treino], digits.target[:treino])

Classifi = clf.predict(digits.data[(treino+1):])

resultado_aC = digits.target[(treino+1):]

#
#for i in range(0,resultado_aC):
#   if resultado_aC[i] == 0:
#       certo=0
#       certo+=1
#   else:
#       errado=0  
#       errado+=1
#




