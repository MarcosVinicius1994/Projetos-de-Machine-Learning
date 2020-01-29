# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:54:57 2019

@author: Marcos Vinicius Timoteo Nunes
Matricula: 16.2.8388

Professor: Luiz Carlos Bambirra
Disciplina: Linguagens de Programação 
Turma: Noite
"""

vetor = ['mae(elizabeth,charles)'
         ,'pai(charles,harry)'
         ,'pai(charles,willian)'] 

def func(X):
    for i in range(len(vetor)):
        if( X == vetor[i]):
            print('true') 
            break
        elif (X =='neto(willian,elizabeth)' or  X == 'avó(elizabeth,willian)'):
             if(vetor[i] == 'mae(elizabeth,charles)' or vetor[i]=='pai(charles,willain'):
                 print('true')
                 break
        elif (X =='irmão(willian,harry)' or X== 'irmão(harry,willian)'):
             if(vetor[i] == 'pai(charles,harry)' and 'pai(charles,willian)'):
                 print('true')
                 break
        else:
            print('false')
            break
                 
        
#        
#Regras de entrada: (Regras que podem ser pesquisadas)
#    1° 'pai(charles,willian)'
#    2° 'pai(charles,harry)'
#    3° 'mae(elizabeth,charles)'
#    4° 'neto(willian,elizabeth)'
#    5° 'avó(elizabeth,willian)'
#    6° 'irmão(willian,harry)'
#    7° 'irmão(harry,willian)'
            
    