# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 20:07:22 2019

@author: marco
"""
from sklearn import datasets
from sklearn import svm




from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1,2],[1,4],[1,0],[10,2],[10,4],[10,0]])

KMeans = KMeans(n_clusters = 2, random_state=0).fit(X)
KMeans.labels_
KMeans.predict([[0,0],[12,3]])
KMeans.cluster_centers_