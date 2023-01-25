import copy
import numpy as np
from funcoesAuxiliares import *

def novoEstado(estadoAtual, estadoFinal):
    h = distanciaManhattan(estadoAtual, estadoFinal)
    return estado(estadoAtual, 0, h)

def buscaGulosa(estadoInicial, estadoFinal):
    fronteira = []
    custoCaminho = 0
    tam_fronteira = []
    visitados = []

    inicial = novoEstado(estadoInicial, estadoFinal)
    insereEstado(inicial, fronteira)
    while len(fronteira) != 0:
        tam_fronteira.append(len(fronteira))
        estadoAtual = fronteira.pop(0)
        custoCaminho+=1
        if estadoAtual.estado == estadoFinal:
            #Estado Atual, Custo do caminho, Custo de espaço, Custo de tempo.
            return estadoAtual.estado, custoCaminho, max(tam_fronteira), custoCaminho
        possiveisJogadas = estadosPossiveis(estadoAtual)
        for proximoEstado in possiveisJogadas:
            if proximoEstado not in visitados:
                insereEstado(novoEstado(proximoEstado, estadoFinal), fronteira)
                visitados.append(proximoEstado)
    return 0

estadoInicial = [[1,2,3],[4,5,6],[0,7,8]]
estadoFinal = [[1,2,3],[4,5,6],[7,8,0]]
print(buscaGulosa(estadoInicial, estadoFinal))