import copy
import numpy as np
from funcoesAuxiliares import *

def novoEstado(estadoAtual, estadoFinal, g=0):
    h = g + distanciaManhattan(estadoAtual, estadoFinal)
    return estado(estadoAtual, g, h)

def buscaAEstrela(estadoInicial, estadoFinal):
    fronteira = []
    custoCaminho = 0
    tam_fronteira = []
    visitados = []

    inicial = novoEstado(estadoInicial, estadoFinal, g=0)
    insereEstado(inicial, fronteira)
    while len(fronteira) != 0:
        tam_fronteira.append(len(fronteira))
        estadoAtual = fronteira.pop(0)
        print('Estado Atual: \n', np.array(estadoAtual.estado).reshape(3, 3))
        custoCaminho+=1
        if estadoAtual.estado == estadoFinal:
            #Estado Atual, Custo do caminho, Custo de espaço, Custo de tempo.
            return estadoAtual.estado, custoCaminho, max(tam_fronteira), custoCaminho
        possiveisJogadas = estadosPossiveis(estadoAtual)
        for proximoEstado in possiveisJogadas:
            if proximoEstado not in visitados:
                print('Proximo estado: \n', np.array(proximoEstado).reshape(3, 3))
                insereEstado(novoEstado(proximoEstado, estadoFinal, estadoAtual.g+1), fronteira)
                visitados.append(proximoEstado)

    return 0

estadoInicial = [[1,2,3],[4,5,6],[0,7,8]]
estadoFinal = [[1,2,3],[4,5,6],[7,8,0]]
print(buscaAEstrela(estadoInicial, estadoFinal))