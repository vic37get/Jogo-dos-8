import numpy as np


def estadosPossiveis(estadoAtual):
    espacoEmBranco = estadoAtual.index(0)
    print("espacoEmBranco: ", espacoEmBranco)
    x, y = espacoEmBranco // 3, espacoEmBranco % 3
    print("X: ", x, "Y: ", y)
    movimentacoes = []
    if x > 0:
        movePraBaixo = estadoAtual[:]
        movePraBaixo[espacoEmBranco], movePraBaixo[espacoEmBranco - 3] = (
            movePraBaixo[espacoEmBranco - 3],
            movePraBaixo[espacoEmBranco],
        )
        print("movePraBaixo: \n", np.array(movePraBaixo).reshape(3, 3))
        movimentacoes.append(movePraBaixo)
    if x < 2:
        movePraCima = estadoAtual[:]
        movePraCima[espacoEmBranco], movePraCima[espacoEmBranco + 3] = (
            movePraCima[espacoEmBranco + 3],
            movePraCima[espacoEmBranco],
        )
        print("movePraCima: \n", np.array(movePraCima).reshape(3, 3))
        movimentacoes.append(movePraCima)
    if y > 0:
        movePraDireita = estadoAtual[:]
        print("movePraDireita: \n", np.array(movePraDireita).reshape(3, 3))
        movimentacoes.append(movePraDireita)
    if y < 2:
        movePraEsquerda = estadoAtual[:]
        movePraEsquerda[espacoEmBranco], movePraEsquerda[espacoEmBranco + 1] = (
            movePraEsquerda[espacoEmBranco + 1],
            movePraEsquerda[espacoEmBranco],
        )
        print("movePraEsquerda: \n", np.array(movePraEsquerda).reshape(3, 3))
        movimentacoes.append(movePraEsquerda)
    return movimentacoes
