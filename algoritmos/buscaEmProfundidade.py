import numpy as np
from funcoesAuxiliares import estadosPossiveisBuscaCega


def buscaEmProfundidadeMain(estadoInicial, estadoFinal):
    iteracoes = []
    nosGerados = 0

    custoCaminho = 0
    tam_fronteira = []

    profundidadeMaxima = 0
    profundidadeSolucao = 0
    fronteiraEstados = []
    fronteiraEstados.append((estadoInicial, 0))
    estadosVisitados = []

    while len(fronteiraEstados) != 0:
        tam_fronteira.append(len(fronteiraEstados))
        estadoAtual, profundidade = fronteiraEstados.pop()
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
            iteracoes.append([estadoAtual, '', custoCaminho, len(fronteiraEstados), nosGerados, profundidadeSolucao, profundidadeMaxima])
            #Estado Atual, Custo do caminho, Custo de espaço, Custo de tempo.
            return estadoAtual, custoCaminho, max(tam_fronteira), custoCaminho, profundidadeSolucao, profundidadeMaxima, iteracoes
        # Se ainda não foi, o nó é ampliado.
        estadosIteracoes = []
        for proximoEstado in possiveisJogadas:
            if proximoEstado not in estadosVisitados:
                # Adicionando na fronteira de espaço de estados.
                fronteiraEstados.append((proximoEstado, profundidade + 1))
                estadosVisitados.append(proximoEstado)
                print('Estado gerado: \n', np.array(proximoEstado).reshape(3,3))
                print('Profundidade: ', profundidade+1)
                estadosIteracoes.append(np.array(proximoEstado).reshape(1,-1))
                nosGerados+=1
            else:
                print("O estado {} ja foi visitado".format(tuple(proximoEstado)))
        iteracoes.append([estadoAtual, estadosIteracoes, custoCaminho, len(fronteiraEstados), nosGerados, profundidadeSolucao, profundidadeMaxima])
    return None


'''estadoInicial = [[1,2,3],[4,5,6],[0,7,8]]
estadoFinal = [[1,2,3],[4,5,6],[7,8,0]]
print(buscaEmProfundidadeMain(estadoInicial, estadoFinal))'''