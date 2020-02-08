import numpy as np
import matplotlib.pyplot as plt
import pandas as table


from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

from sklearn.cluster import KMeans

database = table.read_table('arquivoTreino.data',delimiter=',')
database = database.iloc[:,1:11]
#
#database.drop('1000025', inplace=True, axis=1)

#teste...

#Dados randomicos no database
r = np.random.permutation(len(database))

base2 = database.iloc[r,:]


#Dados de treino (70% dos dados)
treino = base2.iloc[0:np.int(np.floor(len(base2)*0.7)),:]

#Dados de teste (30% dos dados)
teste = base2.iloc[0:np.int(np.floor(len(base2)*0.3)),:]


#DataTrain recebe os dados de treino, menos a coluna de valores de classificação
DataTrain = treino.iloc[:,0:9]


#Aux recebe os valores da coluna de dados de classificação
aux = base2.iloc[:,9:10]


#True recebendo os valores boleanos para a entrada 4(True onde é 4 e false para o restante)
true = aux == 4

#Onde é true, ou 4 recebera 1
aux.iloc[true]=1

#True recebendo os valores boleanos para a entrada 2(True onde é 4 e false para o restante)
true = aux == 2

#Onde é false, ou 2 recebera -1
aux.iloc[true] = -1

saida_Treino  = aux.iloc[0:np.int(np.floor(len(aux)*0.7)),:]
saida_Teste =  aux.iloc[0:np.int(np.floor(len(aux)*0.3)),:]


classifier = KNeighborsClassifier(n_neighbors=3)

classifier.fit(DataTrain, saida_Treino)

Pred = classifier.predict(teste.iloc[:,0:9])



print(confusion_matrix(saida_Teste, Pred))
print(classification_report(saida_Teste, Pred))

#
#Kmeans = KMeans(n_clusters = 9, random_state=0).fit(DataTrain, saida_Treino)
#Kmeans.predict(teste.iloc[:,0:9])





retiraUl = base2.iloc[:,0:9]

retiraPrim = retiraUl.iloc[:,1:9]

Kmeans = KMeans(n_clusters = 2, random_state=0).fit(retiraPrim)
Kmeans.labels_
Aux = Kmeans.predict(retiraPrim)
Kmeans.cluster_centers_


for i in range(len(Aux)):
    if Aux[i]== 1:
     Aux[i]=1
    else:
     Aux[i]=-1





#Calculo de sensibilidade e especificidade
#
#VP = 0
#VN = 0
#for i in range(len(Pred)):
#    if Pred[i]== 1:
#     VP +=1
#    else:
#     VN +=1
#print(VP)
#print(VN)

Vanterior = sum(saida_Teste.iloc[:,0]==1)

Fanterior  = sum(saida_Teste.iloc[:,0]==-1)
