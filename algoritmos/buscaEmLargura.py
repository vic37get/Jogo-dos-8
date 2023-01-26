import queue
import numpy as np
from funcoesAuxiliares import estadosPossiveisBuscaCega


def buscaEmLarguraMain(estadoInicial, estadoFinal):
    iteracoes = []
    nosGerados = 0

    custoCaminho = 0
    tam_fronteira = []
    estadosVisitados = []  
    profundidadeMaxima = 0
    profundidadeSolucao = 0
    fronteiraEstados = queue.Queue()
    fronteiraEstados.put((estadoInicial, 0))



    while not fronteiraEstados.empty():
        tam_fronteira.append(fronteiraEstados.qsize())
        estadoAtual, profundidade = fronteiraEstados.get()
        if estadoAtual not in estadosVisitados:
            estadosVisitados.append(estadoAtual)
        custoCaminho+=1
        print('\nEstado atual: \n', np.array(estadoAtual).reshape(3,3))
        print('Profundidade: ', profundidade)
        possiveisJogadas = estadosPossiveisBuscaCega(estadoAtual)
        # Se a solução foi encontrada.
        profundidadeMaxima = max(profundidadeMaxima, profundidade)
        if estadoAtual == estadoFinal:
            profundidadeSolucao = profundidade
            iteracoes.append([estadoAtual, '', custoCaminho, fronteiraEstados.qsize(), nosGerados, profundidadeSolucao, profundidadeMaxima])
            #Estado Atual, Custo do caminho, Custo de espaço, Custo de tempo.
            return estadoAtual, custoCaminho, max(tam_fronteira), custoCaminho, profundidadeSolucao, profundidadeMaxima, iteracoes
        # Se ainda não foi, o nó é ampliado.
        estadosIteracoes = []
        for proximoEstado in possiveisJogadas:
            if proximoEstado not in estadosVisitados:
                # Adicionando na fronteira de espaço de estados.
                fronteiraEstados.put((proximoEstado, profundidade + 1))
                estadosVisitados.append(proximoEstado)
                print('Estado gerado: \n', np.array(proximoEstado).reshape(3,3))
                print('Profundidade: ', profundidade+1)
                estadosIteracoes.append(np.array(proximoEstado).reshape(1,-1))
                nosGerados+=1
            else:
                print("\nO estado {} ja foi visitado".format(tuple(proximoEstado)))
        iteracoes.append([estadoAtual, estadosIteracoes, custoCaminho, fronteiraEstados.qsize(), nosGerados, profundidadeSolucao, profundidadeMaxima])
    return None

'''estadoInicial = [[1,2,3],[4,5,6],[0,7,8]]
estadoFinal = [[1,2,3],[4,5,6],[7,8,0]]
print(buscaEmLarguraMain(estadoInicial, estadoFinal))'''
