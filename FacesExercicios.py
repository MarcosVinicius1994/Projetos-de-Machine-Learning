# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 19:36:16 2019

@author: 	Marcos Vinicius Timoteo Nunes Matricula: 16.2.8388
Professor: Luiz Carlos Bambirra
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_olivetti_faces
from sklearn.utils.validation import check_random_state

from sklearn.ensemble import ExtraTreesRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import Lasso


# Carregamento das faces para a base de dados
data = fetch_olivetti_faces()
digits = fetch_olivetti_faces()
	

targets = data.target

data = data.images.reshape((len(data.images), -1))


#Separando os dados para treinamento e teste
train = data[targets < 30]
test = data[targets >= 30]  # Test on independent people

# Decidindo o numero de faces
n_faces = 5


rng = check_random_state(4)
face_ids = rng.randint(test.shape[0], size=(n_faces, ))
test = test[face_ids, :]

n_pixels = data.shape[1]
# Dados de treino (dividindo os pixels para treino)
X_train = train[:, :(n_pixels + 1) // 2]
y_train = train[:, n_pixels // 2:]

# Dados de teste (dividindo os pixels teste)
X_test = test[:, :(n_pixels + 1) // 2]
y_test = test[:, n_pixels // 2:]


# Chamada dos metodos de classificação através de um json
ESTIMATORS = {
    "Extra trees": ExtraTreesRegressor(n_estimators=10, max_features=32,
                                       random_state=0),
    "K-nn": KNeighborsRegressor(),
    "Linear regression": LinearRegression(),
    "Ridge": RidgeCV(),
	"Lasso" : Lasso(),
}


#Treinando o algoritmo
y_test_predict = dict()
for name, estimator in ESTIMATORS.items():
    estimator.fit(X_train, y_train)
    y_test_predict[name] = estimator.predict(X_test)

# Plot das imagens no console
image_shape = (64, 64)

n_cols = 1 + len(ESTIMATORS)
plt.figure(figsize=(2. * n_cols, 2.26 * n_faces))
plt.suptitle("Face completion with multi-output estimators", size=16)

for i in range(n_faces):
    true_face = np.hstack((X_test[i], y_test[i]))

    if i:
        sub = plt.subplot(n_faces, n_cols, i * n_cols + 1)
    else:
        sub = plt.subplot(n_faces, n_cols, i * n_cols + 1,
                          title="true faces")

    sub.axis("off")
    sub.imshow(true_face.reshape(image_shape),
               cmap=plt.cm.gray,
               interpolation="nearest")

 #Completando as faces com os resultados dos algoritimos
    for j, est in enumerate(sorted(ESTIMATORS)):
        completed_face = np.hstack((X_test[i], y_test_predict[est][i]))

        if i:
            sub = plt.subplot(n_faces, n_cols, i * n_cols + 2 + j)

        else:
            sub = plt.subplot(n_faces, n_cols, i * n_cols + 2 + j,
                              title=est)

        sub.axis("off")
        sub.imshow(completed_face.reshape(image_shape),
                   cmap=plt.cm.gray,
                   interpolation="nearest")
		
plt.show()

acertos =0
erros =0
normal =0
#Calculando a quantidade de acertos




#for i in y_test_predict:
#	ResultValor = y_test_predict[i]
#	Result_X_test = X_test[i]
#	for j in ResultValor:
#		Valor = ResultValor[j] - Result_X_test[j]
#		print('Algoritimo:',name )
#		print(Valor)

#

#Função para calcular o numero de acertos dos algoritmos
for i, est in enumerate(sorted(ESTIMATORS)):
 result = ( X_train- y_test_predict[est][i])
 for i in range(len(result)):
	 VetorInicialPixels = X_train[i]
	 for x in range(len(result)):
		 ValorInicialPixels=  VetorInicialPixels[x]
		 valor = x
		 if x > ValorInicialPixels:
			 acertos +=1
		 elif x == ValorInicialPixels:
			 normal+=1
		 else:
			 erros+=1
		 
		 
		 
#  Impressão do numero de erros e acertos dos algoritmos
print ('Quantidade de erros', erros)
print ('Quantidade de acertos',acertos)
print ('Quantidade de valores iguais a zero', normal)

#
#
#	
	
	




