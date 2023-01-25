import numpy as np
from utils import estadosPossiveis


def buscaEmProfundidadeMain(estadoInicial, estadoFinal):
    iteracoes = []
    nosGerados = 0
    profundidadeMaxima = 0
    jogada = 0
    profundidadeSolucao = None
    fronteiraEstados = []
    fronteiraEstados.append((estadoInicial, 0))
    jaGerados = set()
    jaGerados.add(tuple(estadoInicial))
    
    estadosVisitados = set()
    estadosVisitados.add(tuple(estadoInicial))

    while len(fronteiraEstados) != 0:
        jogada+=1
        #print("ESPAÇO DE ESTADOS: \n", fronteiraEstados)
        estadoAtual, profundidade = fronteiraEstados.pop()
        estadosVisitados.add(tuple(estadoAtual))
        print("ESTADO ATUAL: \n", np.array(estadoAtual).reshape(3, 3))
        possiveisJogadas = estadosPossiveis(estadoAtual)

        # Se a solução foi encontrada.
        profundidadeMaxima = max(profundidadeMaxima, profundidade)
        if estadoAtual == estadoFinal:
            profundidadeSolucao = profundidade
            iteracoes.append([estadoAtual, '', len(estadosVisitados), nosGerados, len(fronteiraEstados), profundidadeSolucao, profundidadeMaxima, jogada])
            return (
                estadoAtual,
                len(fronteiraEstados),
                nosGerados,
                profundidadeMaxima,
                profundidadeSolucao,
                len(estadosVisitados), iteracoes, jogada
            )
        # Se ainda não foi, o nó é ampliado.
        estadosNaoRepetidos = []
        for proximoEstado in possiveisJogadas:
            print("Proximo estado:\n",np.array(proximoEstado).reshape(3, 3),"\n///////////",)
            if tuple(proximoEstado) not in jaGerados:
                # Adicionando na fronteira de espaço de estados.
                fronteiraEstados.append((proximoEstado, profundidade + 1))
                estadosNaoRepetidos.append(proximoEstado)
                jaGerados.add(tuple(proximoEstado))
                nosGerados += 1
            else:
                print("O estado {} ja foi visitado".format(tuple(proximoEstado)))
                
        iteracoes.append([estadoAtual, estadosNaoRepetidos, len(estadosVisitados), nosGerados, len(fronteiraEstados), profundidadeSolucao, profundidadeMaxima, jogada])
    return None