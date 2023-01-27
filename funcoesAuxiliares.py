import copy
import random

# Classe estado, que tem a configuração de um estado. 
# (estado do tabuleiro, nó pai, custo do caminho e 
# estimativa de distancia da solução)
class estado:
    def __init__(self, estado, nopai, g, h):
        self.estado = estado
        self.nopai = nopai
        self.g = g
        self.h = h

#Função que gera os possíveis movimentos do tabuleiro a partir de um estado.
def estadosPossiveis(estadoAtual):
    linha, coluna = encontraNumEstado(estadoAtual, 0)
    movimentacoes = []

    if linha > 0:
        movePraCima = copy.deepcopy(estadoAtual)
        movePraCima[linha-1][coluna], movePraCima[linha][coluna] = movePraCima[linha][coluna], movePraCima[linha-1][coluna]
        movimentacoes.append(movePraCima)

    if linha < 2:
        movePraBaixo = copy.deepcopy(estadoAtual)
        movePraBaixo[linha+1][coluna], movePraBaixo[linha][coluna] = movePraBaixo[linha][coluna], movePraBaixo[linha+1][coluna]
        movimentacoes.append(movePraBaixo)
    
    if coluna > 0:
        movePraEsquerda = copy.deepcopy(estadoAtual)
        movePraEsquerda[linha][coluna-1], movePraEsquerda[linha][coluna] = movePraEsquerda[linha][coluna], movePraEsquerda[linha][coluna-1]
        movimentacoes.append(movePraEsquerda)
    
    if coluna < 2:
        movePraDireita = copy.deepcopy(estadoAtual)
        movePraDireita[linha][coluna+1], movePraDireita[linha][coluna] = movePraDireita[linha][coluna], movePraDireita[linha][coluna+1]
        movimentacoes.append(movePraDireita)
    #Os movimentos são aleatorizados na tentativa de minimizar possíveis loops.
    random.shuffle(movimentacoes)
    return movimentacoes

# Função que retorna as coordenadas (localização)
# de um numero dentro do tabuleiro.
def encontraNumEstado(estado, numero):
    for i in range(3):
        for j in range(3):
            if estado[i][j] == numero:
                return i,j

# Função Heurística Distancia de Manhathan. 
# (É a soma das distância de todos os números do tabuleiro 
# do estado Meta, ou seja, o quão cada peça está distante da 
# posição correta.)
def distanciaManhattan(estadoAtual, estadoFinal):
    dist = 0
    fora = 0
    for i in range(3):
        for j in range(3):
            if estadoAtual[i][j] == 0:
                continue
            i2, j2 = encontraNumEstado(estadoFinal, estadoAtual[i][j])
            if i2 != i or j2 !=j:
                fora +=1
            dist += abs(i2-i) + abs(j2-j)
    return dist + fora

# Função que insere um estado na fronteira de espaço 
# de estados e a ordena por menor custo. 
# (Usada somente nos algoritmos Busca A* e Busca Gulosa.)
def insereEstado(estado, fronteira):
    if estado in fronteira:
        return fronteira
    fronteira.append(estado)
    chave = fronteira[-1]
    j = len(fronteira)-2
    while fronteira[j].h > chave.h and j>=0:
        fronteira[j+1] = fronteira[j]
        fronteira[j] = chave
        j-=1
    return fronteira
