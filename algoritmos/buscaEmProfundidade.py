import numpy as np
from utils import estadosPossiveis


def buscaEmLargura(estadoInicial, estadoFinal):
    nosGerados = 0
    profundidadeMaxima = 0
    profundidadeSolucao = None
    fronteiraEstados = []
    fronteiraEstados.append((estadoInicial, 0))
    estadosVisitados = set()
    estadosVisitados.add(tuple(estadoInicial))

    while len(fronteiraEstados) != 0:
        print("ESPAÇO DE ESTADOS: \n", fronteiraEstados)
        estadoAtual, profundidade = fronteiraEstados.pop()
        print("ESTADO ATUAL: \n", np.array(estadoAtual).reshape(3, 3))
        estadosVisitados.add(tuple(estadoAtual))
        # Se a solução foi encontrada.
        profundidadeMaxima = max(profundidadeMaxima, profundidade)
        if estadoAtual == estadoFinal:
            profundidadeSolucao = profundidade
            return (
                estadoAtual,
                len(fronteiraEstados),
                nosGerados,
                profundidadeMaxima,
                profundidadeSolucao,
                len(estadosVisitados),
            )
        # Se ainda não foi, o nó é ampliado.
        for proximoEstado in estadosPossiveis(estadoAtual):
            print(
                "Proximo estado:\n",
                np.array(proximoEstado).reshape(3, 3),
                "\n///////////",
            )
            if tuple(proximoEstado) not in estadosVisitados:
                # Adicionando na fronteira de espaço de estados.
                fronteiraEstados.append((proximoEstado, profundidade + 1))
                nosGerados += 1
            else:
                print("O estado {} ja foi visitado".format(tuple(proximoEstado)))
    return None


def main():
    # exemplo de teste
    estadoInicial = [1, 2, 3, 4, 5, 6, 0, 7, 8]
    estadoFinal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    (
        solucao,
        fronteira,
        nosGerados,
        profundidadeMaxima,
        profundidadeSolucao,
        estadosVisitados,
    ) = buscaEmLargura(estadoInicial, estadoFinal)
    if solucao:
        print(
            "Solução: ",
            solucao,
            "\nFronteira de espaço de estados: ",
            fronteira,
            "\nNós Gerados: ",
            nosGerados,
            "\nProfundidade Maxima: ",
            profundidadeMaxima,
            "\nProfundidade da Solução: ",
            profundidadeSolucao,
            "\nTempo gasto: ",
            estadosVisitados + nosGerados,
        )
    else:
        print("Não foi possível encontrar solução.")


main()
