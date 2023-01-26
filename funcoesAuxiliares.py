import copy

class estado:
    def __init__(self, estado, g, h):
        self.estado = estado
        self.g = g
        self.h = h

def estadosPossiveisBuscaCega(estadoAtual):
    linha, coluna = encontraNumEstado(estadoAtual, 0)
    movimentacoes = []
    if linha < 2:
        movePraBaixo = copy.deepcopy(estadoAtual)
        movePraBaixo[linha+1][coluna], movePraBaixo[linha][coluna] = movePraBaixo[linha][coluna], movePraBaixo[linha+1][coluna]
        #print("movePraBaixo: \n", movePraBaixo)
        movimentacoes.append(movePraBaixo)
    if linha > 0:
        movePraCima = copy.deepcopy(estadoAtual)
        movePraCima[linha-1][coluna], movePraCima[linha][coluna] = movePraCima[linha][coluna], movePraCima[linha-1][coluna]
        #print("movePraCima: \n", movePraCima)
        movimentacoes.append(movePraCima)
    if coluna < 2:
        movePraDireita = copy.deepcopy(estadoAtual)
        movePraDireita[linha][coluna+1], movePraDireita[linha][coluna] = movePraDireita[linha][coluna], movePraDireita[linha][coluna+1]
        #print("movePraDireita: \n", movePraDireita)
        movimentacoes.append(movePraDireita)
    if coluna > 0:
        movePraEsquerda = copy.deepcopy(estadoAtual)
        movePraEsquerda[linha][coluna-1], movePraEsquerda[linha][coluna] = movePraEsquerda[linha][coluna], movePraEsquerda[linha][coluna-1]
        #print("movePraEsquerda: \n", movePraEsquerda)
        movimentacoes.append(movePraEsquerda)
    return movimentacoes

def estadosPossiveis(estadoAtual):
    estadoAtual = estadoAtual.estado
    linha, coluna = encontraNumEstado(estadoAtual, 0)
    movimentacoes = []
    if linha < 2:
        movePraBaixo = copy.deepcopy(estadoAtual)
        movePraBaixo[linha+1][coluna], movePraBaixo[linha][coluna] = movePraBaixo[linha][coluna], movePraBaixo[linha+1][coluna]
        #print("movePraBaixo: \n", movePraBaixo)
        movimentacoes.append(movePraBaixo)
    if linha > 0:
        movePraCima = copy.deepcopy(estadoAtual)
        movePraCima[linha-1][coluna], movePraCima[linha][coluna] = movePraCima[linha][coluna], movePraCima[linha-1][coluna]
        #print("movePraCima: \n", movePraCima)
        movimentacoes.append(movePraCima)
    if coluna < 2:
        movePraDireita = copy.deepcopy(estadoAtual)
        movePraDireita[linha][coluna+1], movePraDireita[linha][coluna] = movePraDireita[linha][coluna], movePraDireita[linha][coluna+1]
        #print("movePraDireita: \n", movePraDireita)
        movimentacoes.append(movePraDireita)
    if coluna > 0:
        movePraEsquerda = copy.deepcopy(estadoAtual)
        movePraEsquerda[linha][coluna-1], movePraEsquerda[linha][coluna] = movePraEsquerda[linha][coluna], movePraEsquerda[linha][coluna-1]
        #print("movePraEsquerda: \n", movePraEsquerda)
        movimentacoes.append(movePraEsquerda)
    return movimentacoes

def encontraNumEstado(estado, numero):
    for i in range(3):
        for j in range(3):
            if estado[i][j] == numero:
                return i,j

def adentroLista(element, lista):
    for i in lista:
        if i[0] == element:
            return False
    return True

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