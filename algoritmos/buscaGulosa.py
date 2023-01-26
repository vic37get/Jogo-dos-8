import numpy as np
from funcoesAuxiliares import *

def novoEstado(estadoAtual, nopai, estadoFinal, g):
    h = distanciaManhattan(estadoAtual, estadoFinal)
    return estado(estadoAtual, nopai, g, h)

def buscaGulosa(estadoInicial, estadoFinal):
    iteracoes = []
    nosGerados = 0
    fronteira = []
    custoCaminho = 0
    tam_fronteira = []
    visitados = []
    profundidadeMaxima = 0

    inicial = novoEstado(estadoInicial, None, estadoFinal, g=0)
    insereEstado(inicial, fronteira)
    while len(fronteira) != 0:
        tam_fronteira.append(len(fronteira))
        estadoAtual = fronteira.pop(0)
        profundidadeMaxima = max(profundidadeMaxima, estadoAtual.g)
        print('Estado Atual: \n', np.array(estadoAtual.estado).reshape(3, 3))
        print('Profundidade: ', estadoAtual.g)
        custoCaminho+=1
        if estadoAtual.estado == estadoFinal:
            iteracoes.append([estadoAtual.estado, '', custoCaminho, len(fronteira), nosGerados, estadoAtual.g, profundidadeMaxima])
            #Estado Atual, Custo do caminho, Custo de espaço, Custo de tempo.
            return estadoAtual.estado, custoCaminho, max(tam_fronteira), custoCaminho, estadoAtual.g, profundidadeMaxima, iteracoes
        possiveisJogadas = estadosPossiveis(estadoAtual)
        estadosIteracoes = []
        for proximoEstado in possiveisJogadas:
            if proximoEstado not in visitados:
                print('Estado gerado: \n', np.array(proximoEstado).reshape(3,3))
                print('Profundidade: ', estadoAtual.g+1)
                insereEstado(novoEstado(proximoEstado, estadoAtual, estadoFinal, estadoAtual.g+1), fronteira)
                visitados.append(proximoEstado)
                estadosIteracoes.append(np.array(proximoEstado).reshape(1,-1))
                nosGerados+=1
        iteracoes.append([estadoAtual.estado, estadosIteracoes, custoCaminho, len(fronteira), nosGerados, estadoAtual.g, profundidadeMaxima])
    return 0

#estadoInicial = [[1,2,3],[4,5,6],[8,7,0]]
#estadoFinal = [[1,2,3],[4,5,6],[7,8,0]]
#buscaGulosa(estadoInicial, estadoFinal)
