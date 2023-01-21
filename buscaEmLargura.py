import queue
import numpy as np

def buscaEmLargura(estadoInicial, estadoFinal):
    nosGerados = 0
    profundidadeMaxima = 0
    profundidadeSolucao = None
    fronteiraEstados = queue.Queue()
    fronteiraEstados.put((estadoInicial, 0))
    estadosVisitados = set()
    estadosVisitados.add(tuple(estadoInicial))

    while not fronteiraEstados.empty():
        print('ESPAÇO DE ESTADOS: \n', fronteiraEstados.queue)
        estadoAtual, profundidade = fronteiraEstados.get()
        estadosVisitados.add(tuple(estadoAtual))
        #Se a solução foi encontrada.
        if estadoAtual == estadoFinal:
            profundidadeSolucao = profundidade
            return estadoAtual, fronteiraEstados.qsize(), nosGerados, profundidadeMaxima, profundidadeSolucao, len(estadosVisitados)
        profundidadeMaxima = max(profundidadeMaxima, profundidade)
        #Se ainda não foi, o nó é ampliado.
        for proximoEstado in estadosPossiveis(estadoAtual):
            print('Proximo estado:\n', np.array(proximoEstado).reshape(3,3), '\n///////////')
            if tuple(proximoEstado) not in estadosVisitados:
                #Adicionando na fronteira de espaço de estados.
                fronteiraEstados.put((proximoEstado, profundidade+1))
                nosGerados+=1
            else:
                print('O estado {} ja foi visitado'.format(tuple(proximoEstado)))
    return None

def estadosPossiveis(estadoAtual):
    espacoEmBranco = estadoAtual.index(0)
    print('espacoEmBranco: ',espacoEmBranco)
    x, y = espacoEmBranco // 3, espacoEmBranco % 3
    print('X: ', x ,'Y: ', y)
    movimentacoes = []
    if x > 0:
        movePraBaixo = estadoAtual[:]
        movePraBaixo[espacoEmBranco], movePraBaixo[espacoEmBranco-3] = movePraBaixo[espacoEmBranco-3], movePraBaixo[espacoEmBranco]
        print('movePraBaixo: \n',np.array(movePraBaixo).reshape(3,3))
        movimentacoes.append(movePraBaixo)
    if x < 2:
        movePraCima = estadoAtual[:]
        movePraCima[espacoEmBranco], movePraCima[espacoEmBranco+3] = movePraCima[espacoEmBranco+3], movePraCima[espacoEmBranco]
        print('movePraCima: \n',np.array(movePraCima).reshape(3,3))
        movimentacoes.append(movePraCima)
    if y > 0:
        movePraDireita = estadoAtual[:]
        print('movePraDireita: \n',np.array(movePraDireita).reshape(3,3))
        movimentacoes.append(movePraDireita)
    if y < 2:
        movePraEsquerda = estadoAtual[:]
        movePraEsquerda[espacoEmBranco], movePraEsquerda[espacoEmBranco+1] = movePraEsquerda[espacoEmBranco+1], movePraEsquerda[espacoEmBranco]
        print('movePraEsquerda: \n',np.array(movePraEsquerda).reshape(3,3))
        movimentacoes.append(movePraEsquerda)
    return movimentacoes


def main():
    # exemplo de teste
    estadoInicial = [1, 2, 3, 4, 5, 6, 0, 7, 8]
    estadoFinal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    solucao, fronteira, nosGerados, profundidadeMaxima, profundidadeSolucao, estadosVisitados = buscaEmLargura(estadoInicial, estadoFinal)
    if solucao:
        print('Solução: ', solucao, '\nFronteira de espaço de estados: ', fronteira, '\nNós Gerados: ', nosGerados, '\nProfundidade Maxima: ',
        profundidadeMaxima, '\nProfundidade da Solução: ', profundidadeSolucao, '\nTempo gasto: ', (estadosVisitados*2)+nosGerados)
    else:
        print("Não foi possível encontrar solução.")

main()
