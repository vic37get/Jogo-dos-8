import numpy as np
from funcoesAuxiliares import *

def buscaEmProfundidadeMain(estadoInicial, estadoFinal):
    iteracoes = []
    nosGerados = 0
    custoCaminho = 0
    tam_fronteira = []
    profundidadeMaxima = 0
    fronteiraEstados = []
    fronteiraEstados.append(estado(estadoInicial, None, 0, None))
    estadosVisitados = []

    while len(fronteiraEstados) != 0:
        tam_fronteira.append(len(fronteiraEstados))
        estadoAtual = fronteiraEstados.pop()
        if estadoAtual.estado not in estadosVisitados:
            estadosVisitados.append(estadoAtual.estado)
        custoCaminho+=1
        print('\nEstado atual: \n', np.array(estadoAtual.estado).reshape(3,3))
        print('Profundidade: ', estadoAtual.g)
        possiveisJogadas = estadosPossiveis(estadoAtual.estado)
        # Se a solução foi encontrada.
        profundidadeMaxima = max(profundidadeMaxima, estadoAtual.g)
        if estadoAtual.estado == estadoFinal:
            iteracoes.append([estadoAtual.estado, '', custoCaminho, len(fronteiraEstados), nosGerados, estadoAtual.g, profundidadeMaxima])
            #Estado Atual, Custo do caminho, Custo de espaço, Custo de tempo.
            return estadoAtual.estado, custoCaminho, max(tam_fronteira), custoCaminho, estadoAtual.g, profundidadeMaxima, iteracoes
        # Se ainda não foi, o nó é ampliado.
        estadosIteracoes = []
        for proximoEstado in possiveisJogadas:
            if proximoEstado not in estadosVisitados:
                # Adicionando na fronteira de espaço de estados.
                fronteiraEstados.append(estado(proximoEstado, estadoAtual, estadoAtual.g+1, None))
                estadosVisitados.append(proximoEstado)
                print('Estado gerado: \n', np.array(proximoEstado).reshape(3,3))
                print('Profundidade: ', estadoAtual.g+1)
                estadosIteracoes.append(np.array(proximoEstado).reshape(1,-1))
                nosGerados+=1
            else:
                print("O estado {} ja foi visitado".format(tuple(proximoEstado)))
        iteracoes.append([estadoAtual.estado, estadosIteracoes, custoCaminho, len(fronteiraEstados), nosGerados, estadoAtual.g, profundidadeMaxima])
    return None

'''estadoInicial = [[4,1,3],[7,2,5],[0,8,6]]
estadoFinal = [[1,2,3],[4,5,6],[7,8,0]]
print(buscaEmProfundidadeMain(estadoInicial, estadoFinal))'''
