# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 19:35:10 2019

@author: marco
"""


import matplotlib.pyplot as plt
import pandas as table
import numpy as np

from sklearn import datasets
from sklearn import svm

brestCancer = datasets.load_breast_cancer()
#
#iris = datasets.load_iris()
#digits = datasets.load_digits()

#digits.data é a base de dados e target é a classe


for i in range(len(brestCancer)):
     j=i+1 
     if j in range(len(brestCancer)):
#         lista= brestCancer.data[:,(i,j)]   
#        
        clf = svm.SVC(gamma=0.001,C=100.)
        clf.fit(brestCancer.data[:,range(i,j)], brestCancer.target)
        clf.predict(brestCancer.data[:,range(i,j)])