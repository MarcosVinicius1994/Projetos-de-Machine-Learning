# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:38:59 2019

@author: marco
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

k=3

print("\n teste");

a = np.zeros((10,2))
mean1 =[2,2]
cov1 = [[1,0],[0,1]]
N1 =5

classe_1 = np.random.multivariate_normal(mean1,cov1,N1)
fig, ax =plt.subplots()
ax.scatter(classe_1[:,0],classe_1[:,1],c='blue',alpha=0.7,edgecolors='none')


mean2 =[6,6]
cov2 = [[1,0],[0,1]]
N2 =5

classe_2 = np.random.multivariate_normal(mean2,cov2,N2)


ax.scatter(classe_2[:,0],classe_2[:,1],c='yellow',alpha=0.9,edgecolors='none')

ponto_teste =[4,4]

#ax.scatter(ponto_teste[0],ponto_teste[1], c='red',alpha=0.6)
##ax.scatter(classe_1[1,0],classe_1[1,1],c='green',alpha=0.4)
##distancia = np.linalg.norm(classe_1[0,0:1] - ponto_teste)

X = np.concatenate((classe_1, classe_2))

labels = np.concatenate((np.repeat(1,len(classe_1)),np.repeat(-1,len(classe_2))))

"distancia = np.zeros((10,1))"

distancia = np.zeros((len(X),1))

seq=np.arange(1,5.5,0.5)

Z=np.zeros((len(seq),len(seq)))

seq=np.arange(1,5.5,0.5)

for i_grid in range(0,len(seq)):
   for j_grid in range(0,len(seq)):
      ponto_teste= [seq[i_grid],seq[j_grid]]
      distancia = np.zeros((len(X),1))

      for i in range(0,N1+N2):
        distancia[i]=np.linalg.norm(X[i] - ponto_teste)
     
      distancia = np.concatenate((distancia,labels.reshape(N1+N2,1)),axis=1)
     
      distancia_ord =distancia[distancia[:,0].argsort()]
     



      if sum(distancia_ord[0:k,1])<0:
         Z[i_grid,j_grid] =-1
      else:
       Z[i_grid,j_grid] =1
       
       
       
 fig, ax2 =plt.subplots(nrows=1)

ax2.countour(seq, seq, Z, Levels=0, linewidths=1, colors='k')
ctr1 = ax2.contourf(seq, seq, Z, levels=1, alpha=0.3, colors=['red','blue'])     