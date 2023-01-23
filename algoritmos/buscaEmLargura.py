import queue
import numpy as np
from utils import estadosPossiveis


def buscaEmLarguraMain(estadoInicial, estadoFinal):
    iteracoes = []
    nosGerados = 0
    profundidadeMaxima = 0
    jogada = 0
    profundidadeSolucao = None
    fronteiraEstados = queue.Queue()
    fronteiraEstados.put((estadoInicial, 0))
    estadosVisitados = set()
    estadosVisitados.add(tuple(estadoInicial))

    while not fronteiraEstados.empty():
        jogada+=1
        print("ESPAÇO DE ESTADOS: \n", fronteiraEstados.queue)
        estadoAtual, profundidade = fronteiraEstados.get()
        print("ESTADO ATUAL: \n", np.array(estadoAtual).reshape(3, 3))
        estadosVisitados.add(tuple(estadoAtual))
        possiveisJogadas = estadosPossiveis(estadoAtual)
        
        # Se a solução foi encontrada.
        profundidadeMaxima = max(profundidadeMaxima, profundidade)
        if estadoAtual == estadoFinal:
            profundidadeSolucao = profundidade
            iteracoes.append([estadoAtual, '', (len(estadosVisitados) + nosGerados), nosGerados, fronteiraEstados.qsize(), profundidadeSolucao, profundidadeMaxima, jogada])
            return (
                estadoAtual,
                fronteiraEstados.qsize(),
                nosGerados,
                profundidadeMaxima,
                profundidadeSolucao,
                len(estadosVisitados), iteracoes
            )
        # Se ainda não foi, o nó é ampliado.
        estadosNaoRepetidos = []
        for proximoEstado in possiveisJogadas:
            print("Proximo estado:\n",np.array(proximoEstado).reshape(3, 3),"\n///////////",)
            if tuple(proximoEstado) not in estadosVisitados:
                # Adicionando na fronteira de espaço de estados.
                fronteiraEstados.put((proximoEstado, profundidade + 1))
                estadosNaoRepetidos.append(proximoEstado)
                nosGerados += 1
            else:
                print("O estado {} ja foi visitado".format(tuple(proximoEstado)))
        iteracoes.append([estadoAtual, estadosNaoRepetidos, (len(estadosVisitados) + nosGerados), nosGerados, fronteiraEstados.qsize(), profundidadeSolucao, profundidadeMaxima, jogada])
    return None
