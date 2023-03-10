import copy
import numpy as np
from funcoesAuxiliares import *

#Criação de um novo estado, com cálculo de distancia heurística do estado com base na distância de Manhattan.
#Tem como estimativa (h) a soma do custo de caminho percorrido + a distancia de Manhattan.
def novoEstadoHG(estadoAtual, noPai, estadoFinal, g=0):
    h = g + distanciaManhattan(estadoAtual, estadoFinal)
    return estado(estadoAtual, noPai, g, h)

#Algoritmo A*
def buscaAEstrela(estadoInicial, estadoFinal):
    iteracoes = []
    nosGerados = 0
    fronteira = []
    custoCaminho = 0
    tam_fronteira = []
    visitados = []
    profundidadeMaxima = 0

    inicial = novoEstadoHG(estadoInicial, None, estadoFinal, g=0)
    insereEstado(inicial, fronteira)

    while len(fronteira) != 0:
        tam_fronteira.append(len(fronteira))
        estadoAtual = fronteira.pop(0)
        if estadoAtual.estado not in visitados:
            visitados.append(estadoAtual.estado)
        #Profundidade máxima atingida
        profundidadeMaxima = max(profundidadeMaxima, estadoAtual.g)
        print('Estado Atual: \n', np.array(estadoAtual.estado).reshape(3, 3))
        print('Profundidade: ', estadoAtual.g)
        custoCaminho+=1
        # Se a solução foi encontrada.
        if estadoAtual.estado == estadoFinal:
            iteracoes.append([estadoAtual.estado, '', custoCaminho, len(fronteira), nosGerados, estadoAtual.g, profundidadeMaxima])
            #Estado Atual, Custo do caminho, Custo de espaço, Custo de tempo.
            return estadoAtual.estado, custoCaminho, max(tam_fronteira), custoCaminho, estadoAtual.g, profundidadeMaxima, iteracoes
        # Os movimentos possíveis com o tabuleiro nesse estado.
        possiveisJogadas = estadosPossiveis(estadoAtual.estado)
        # Se a solução ainda não foi encontrada, o nó é ampliado.
        estadosIteracoes = []
        for proximoEstado in possiveisJogadas:
            if proximoEstado not in visitados:
                print('Estado gerado: \n', np.array(proximoEstado).reshape(3, 3))
                print('Profundidade: ', estadoAtual.g+1)
                # Adicionando os estados gerados na fronteira de espaço de estados.
                insereEstado(novoEstadoHG(proximoEstado, estadoAtual, estadoFinal, estadoAtual.g+1), fronteira)
                visitados.append(proximoEstado)
                estadosIteracoes.append(np.array(proximoEstado).reshape(1,-1))
                nosGerados+=1
        iteracoes.append([estadoAtual.estado, estadosIteracoes, custoCaminho, len(fronteira), nosGerados, estadoAtual.g, profundidadeMaxima])
    return 0

'''estadoInicial = [[1,2,3],[4,5,6],[0,7,8]]
estadoFinal = [[1,2,3],[4,5,6],[7,8,0]]
print(buscaAEstrela(estadoInicial, estadoFinal))'''
