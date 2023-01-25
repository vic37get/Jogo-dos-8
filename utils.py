import numpy as np


def estadosPossiveis(estadoAtual):
    espacoEmBranco = estadoAtual.index(0)
    #print("espacoEmBranco: ", espacoEmBranco)
    x, y = espacoEmBranco // 3, espacoEmBranco % 3
    #print("X: ", x, "Y: ", y)
    movimentacoes = []
    if espacoEmBranco > 2:
        movePraBaixo = estadoAtual[:]
        movePraBaixo[espacoEmBranco], movePraBaixo[espacoEmBranco - 3] = movePraBaixo[espacoEmBranco - 3], movePraBaixo[espacoEmBranco]
        #print("movePraBaixo: \n", np.array(movePraBaixo).reshape(3, 3))
        movimentacoes.append(movePraBaixo)
    if espacoEmBranco < 6:
        movePraCima = estadoAtual[:]
        movePraCima[espacoEmBranco], movePraCima[espacoEmBranco + 3] = movePraCima[espacoEmBranco + 3], movePraCima[espacoEmBranco]
        #print("movePraCima: \n", np.array(movePraCima).reshape(3, 3))
        movimentacoes.append(movePraCima)
    if espacoEmBranco > 0 and espacoEmBranco != 3 and espacoEmBranco != 6:
        movePraDireita = estadoAtual[:]
        movePraDireita[espacoEmBranco], movePraDireita[espacoEmBranco-1] = movePraDireita[espacoEmBranco-1], movePraDireita[espacoEmBranco]
        #print("movePraDireita: \n", np.array(movePraDireita).reshape(3, 3))
        movimentacoes.append(movePraDireita)
    if espacoEmBranco >= 0 and espacoEmBranco != 2 and espacoEmBranco != 5 and espacoEmBranco !=8:
        movePraEsquerda = estadoAtual[:]
        movePraEsquerda[espacoEmBranco], movePraEsquerda[espacoEmBranco + 1] = movePraEsquerda[espacoEmBranco + 1], movePraEsquerda[espacoEmBranco]
        #print("movePraEsquerda: \n", np.array(movePraEsquerda).reshape(3, 3))
        movimentacoes.append(movePraEsquerda)
    return movimentacoes