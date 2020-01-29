# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 18:23:54 2019

@author: marco
"""

grafo = {
    'a': ['b', 'd', 'e'],
    'b': ['a', 'c', 'e'],
    'c': ['b', 'e'],
    'd': ['a', 'e'],
    'e': ['a', 'b', 'c', 'd', 'f'],
    'f': ['e']
}

valor_profundidade_entrada = 0
valor_profundidade_saida = 0 
profundidades_entrada_saida = {}
pai = {} 
aresta = {} 
niveis = {}
low = {}
demarcadores = set()
articulacoes = set()


def busca_em_profundidade(grafo, vertice_do_grafo):
    for vertice in grafo:
        low[vertice] = vertice

    pai[vertice_do_grafo] = None 
    qtd_filhos_da_raiz = call_to_busca_em_profundidade(grafo, vertice_do_grafo, 1)
    if qtd_filhos_da_raiz <= 1:
        articulacoes.remove(vertice_do_grafo)

def call_to_busca_em_profundidade(grafo, vertice_do_grafo, nivel):
    global valor_profundidade_entrada, valor_profundidade_saida
    valor_profundidade_entrada += 1 
    profundidades_entrada_saida[vertice_do_grafo] = [valor_profundidade_entrada, None] # anotando profundidade de entrada de vertice_do_grafo
    niveis[vertice_do_grafo] = nivel 

    count_filhos = 0 

    for vizinho in grafo.get(vertice_do_grafo): 
        if not profundidades_entrada_saida.get(vizinho):

            pai[vizinho] = vertice_do_grafo 
            count_filhos += 1 # contando a quantidade de filhos do vertice por arestas de arvore (esse valor soh serah relevante para a raiz (primeira chamada de call_to_busca_em_profundidade feita por busca_em_profundidade))
            # aresta[(vertice_do_grafo, vizinho)] = 'aresta de arvore'
            # print('aresta de arvore')
            # chamada de recursao escolhendo agora esse vizinho como raiz:
            call_to_busca_em_profundidade(grafo, vizinho, nivel + 1) # o proximo vertice estarah um nivel abaixo desse na arvore de busca em profundidade
            # HORA DE TESTAR SE O MEU FILHO TEM UM LOW MELHOR QUE O MEU!
            if niveis[low[vizinho]] < niveis[low[vertice_do_grafo]]: # caso meu filho tenha um low melhor que o meu...
                low[vertice_do_grafo] = low[vizinho] # atualizo o meu low, para o low do meu filho (afinal podemos descer quantas vezes quisermos por arestas de arvore para achar o low, lembram?)
            # NESSE MOMENTO EU JAH SEI SE MEUS FILHOS SAO DEMARCADORES OU NAUM!
            if vizinho in demarcadores:
                # se esse vertice_do_grafo eh pai de um demarcador na arvore de busca em profundidade, entao ele eh uma articulacao!
                articulacoes.add(vertice_do_grafo) # repare que nesse momento, podemos ter sujado o vertice escolhido como raiz da busca, pois pode se tratar de um vertice que "fica nas extremidades do grafo", vamos concertar isso em (*)
        else: # caso o vizinho jah esteja na pilha (jah houve uma chamada de call_to_busca_em_profundidade com parametro vertice_do_grafo=vizinho)
            # testa se esse vizinho jah foi desempilhado (terminou sua chamada de call_to_busca_em_profundidade)
            if not profundidades_entrada_saida[vizinho][1]:
                if pai[vertice_do_grafo] != vizinho: # testando se o vizinho eh o pai do vertice tratado nessa chamada de call_to_busca_em_profundidade
                    # caso o vizinho naum seja o pai do vertice dessa chamada de call_to_busca_em_profundidade, eh hora de...
                    # MOMENTO PARA VISITAR vertice_do_grafo -> vizinho COMO ARESTA DE RETORNO
                    # aresta[(vertice_do_grafo, vizinho)] = 'aresta de retorno'
                    # print('aresta de retorno')
                    # por se tratar de uma aresta de retorno, pode ser que meu vizinho esteja mais proximo da raiz que o meu low...
                    if niveis[vizinho] < niveis[low[vertice_do_grafo]]:
                        low[vertice_do_grafo] = vizinho # ... nesse caso, atualizo meu low
                else:
                    # aresta[(vertice_do_grafo, vizinho)] = 'aresta de arvore'
                    # print('aresta de arvore')
            else:
                # aresta[(vertice_do_grafo, vizinho)] = 'aresta de arvore'
                # print('aresta de arvore')

    valor_profundidade_saida += 1 # atualizando o contador de profundidade de saida
    profundidades_entrada_saida[vertice_do_grafo][1] = valor_profundidade_saida
    # NESSE MOMENTO EU SEI SE ESSE vertice_do_grafo EH UM DEMARCADOR OU NAUM!
    if low[vertice_do_grafo] in (vertice_do_grafo, pai[vertice_do_grafo]): # se meu low sou eu mesmo ou meu pai...
        demarcadores.add(vertice_do_grafo) # ... entao eu sou um demarcador!

    return count_filhos





busca_em_profundidade(grafo, 'a')