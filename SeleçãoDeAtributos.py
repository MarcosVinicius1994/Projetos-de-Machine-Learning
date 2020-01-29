# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 23:15:33 2019

@author: marco


Nome: Marcos Vinicius Timoteo Nunes       Matricula: 16.2.8388
Disciplina: Aprendizagem de Maquina
Professor: Luiz Carlos Bambirra
"""


from sklearn.cluster import KMeans
#from sklearn import KNN
from itertools import combinations
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score

#Leitura da base de dados
dataBase = pd.read_table('arquivoTreino.data',delimiter=',', header=None)

#Separando os classificadores da base de dados
targets = dataBase.iloc[:,10:11]

classifier = KNeighborsClassifier(n_neighbors=5)

#Separando a base de dados dos classificadores
dataBaseAtual = dataBase.iloc[:,1:10]


#aux = dataBase.iloc[:,9:10]

clf = svm.SVC(gamma=0.001,C=100.)
# Separando os valores de classificacção para teste e treino
saida_Treino  = targets.iloc[0:np.int(np.floor(len(targets)*0.7)),:]
saida_Teste =  targets.iloc[0:np.int(np.floor(len(targets)*0.3)),:]

vetAcuracia =list()
NumCombinacoes = 0
for x in range(len(dataBaseAtual)):
      cc = list(combinations(dataBaseAtual.columns,x))
      for c in cc:
          dataAux = pd.DataFrame()  
          for j in c:
#			  Concatenando os valores da dataBaseAtual
#			  nas colunas no dataAux(dataFrame) de acordo
#			  com os indices do dataBaseAtual
              dataAux = pd.concat([dataAux, dataBaseAtual[j]], axis=1)
			  
#			  Separando base de teste dos valores do dataAux
              teste = dataAux.iloc[0:np.int(np.floor(len(dataAux)*0.3)),:]
			  
#			  Separando a base de treino dos valores do dataAUX
              treino =dataAux.iloc[0:np.int(np.floor(len(dataAux)*0.7)),:]
#              print(dataAux)
			  
#			  Pegando o numero de combinações
              NumCombinacoes+=1
			  
#			  Treinando o algoritmo
          classifier.fit(treino, saida_Treino)
		  
#		  Classificando os dados de teste
          Pred = classifier.predict(teste)
			   
#		  Adicionando no vetor de acuracia o calculo das acuracias das 
#		  de atributos combinações
          vetAcuracia.append(accuracy_score(saida_Teste, Pred))  	  
		  
#		  Pegando a melhor acuracia
          MAXpred = max(vetAcuracia)
  
		  
#		  Pegando o menor valor de acuracia
          MINpred = min(vetAcuracia)
print(vetAcuracia)
print('Maior valor de acuracia', MAXpred)  
print('Menor valor de acuracia', MINpred)       
				
			
			

   
   
   
	
	 
		

