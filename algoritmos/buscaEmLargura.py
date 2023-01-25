import queue
import numpy as np
from utils import estadosPossiveis


def buscaEmLarguraMain(estadoInicial, estadoFinal):
    custoCaminho = 0
    tam_fronteira = []

    profundidadeMaxima = 0
    profundidadeSolucao = None
    fronteiraEstados = queue.Queue()
    fronteiraEstados.put((estadoInicial, 0))
    estadosVisitados = []

    while not fronteiraEstados.empty():
        tam_fronteira.append(fronteiraEstados.qsize())
        estadoAtual, profundidade = fronteiraEstados.get()
        custoCaminho+=1
        possiveisJogadas = estadosPossiveis(estadoAtual)
        # Se a solução foi encontrada.
        profundidadeMaxima = max(profundidadeMaxima, profundidade)
        if estadoAtual == estadoFinal:
            profundidadeSolucao = profundidade
            #Estado Atual, Custo do caminho, Custo de espaço, Custo de tempo.
            return estadoAtual, custoCaminho, max(tam_fronteira), custoCaminho
        # Se ainda não foi, o nó é ampliado.
        for proximoEstado in possiveisJogadas:
            if proximoEstado not in estadosVisitados:
                # Adicionando na fronteira de espaço de estados.
                fronteiraEstados.put((proximoEstado, profundidade + 1))
                estadosVisitados.append(proximoEstado)
            else:
                print("O estado {} ja foi visitado".format(tuple(proximoEstado)))
    return None

estadoInicial = [1,2,3,4,5,6,0,7,8]
estadoFinal = [1,2,3,4,5,6,7,8,0]
print(buscaEmLarguraMain(estadoInicial, estadoFinal))
