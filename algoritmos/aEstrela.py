import queue
import numpy as np
from utils import estadosPossiveis


def buscaAEstrela(estadoInicial, estadoFinal):
    iteracoes = []
    nosGerados = 0
    profundidadeMaxima = 0
    jogada = 0
    profundidadeSolucao = None
    fronteiraEstados = queue.Queue()
    fronteiraEstados.put((estadoInicial, 0))
    jaGerados = set()
    jaGerados.add(tuple(estadoInicial))
    
    estadosVisitados = set()
    estadosVisitados.add(tuple(estadoInicial))

    while not fronteiraEstados.empty():
        jogada+=1
        #print("ESPAÇO DE ESTADOS: \n", fronteiraEstados.queue)
        estadoAtual, profundidade = fronteiraEstados.get()
        estadosVisitados.add(tuple(estadoAtual))
        print("ESTADO ATUAL: \n", np.array(estadoAtual).reshape(3, 3))
        possiveisJogadas = estadosPossiveis(estadoAtual)
        
        # Se a solução foi encontrada.
        profundidadeMaxima = max(profundidadeMaxima, profundidade)
        if estadoAtual == estadoFinal:
            profundidadeSolucao = profundidade
            iteracoes.append([estadoAtual, '', len(estadosVisitados), nosGerados, fronteiraEstados.qsize(), profundidadeSolucao, profundidadeMaxima, jogada])
            return(
                estadoAtual,
                fronteiraEstados.qsize(),
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
                fronteiraEstados.put((proximoEstado, profundidade + 1))
                estadosNaoRepetidos.append(proximoEstado)
                jaGerados.add(tuple(proximoEstado))
                nosGerados += 1
            else:
                print("O estado {} ja foi visitado".format(tuple(proximoEstado)))
        iteracoes.append([estadoAtual, estadosNaoRepetidos, len(estadosVisitados), nosGerados, fronteiraEstados.qsize(), profundidadeSolucao, profundidadeMaxima, jogada])
    return None


# Algoritmo A*
# Função busca que utiliza uma função
# heurística como auxílio para calcular
# a solução de maneira mais eficiente e,
# além disso, utiliza uma função g
# para determinar o custo até um nó meta 
# f(n) = h(n) + g(n)
# Função que gera os filhos do nó s, no caso
# as opções de reposicionamento do espaço vazio
# Função para verificar se o movimento é válido

import copy
from heapq import heappush, heappop

def valida(x,y):
    r = True
    if (x < 0 or x > 2): r = False
    if (y < 0 or y > 2): r = False

    return r

def sons(s):
    r = []
    x = None
    y = None

    # localizando 0
    for i in range(len(s)):
        for j in range(len(s[i])):
            if (s[i][j] == 0):
                x = i
                y = j

    # sobe
    vx = x - 1
    vy = y
    if (valida(vx,vy)):
        cover = copy.deepcopy(s)
        t = cover[vx][vy]
        cover[vx][vy] = cover[x][y]
        cover[x][y] = t
        r.append(cover)

    # desce
    vx = x + 1
    vy = y
    if (valida(vx,vy)):
        cover = copy.deepcopy(s)
        t = cover[vx][vy]
        cover[vx][vy] = cover[x][y]
        cover[x][y] = t
        r.append(cover)

    # esquerda
    vx = x
    vy = y - 1
    if (valida(vx,vy)):
        cover = copy.deepcopy(s)
        t = cover[vx][vy]
        cover[vx][vy] = cover[x][y]
        cover[x][y] = t
        r.append(cover)

        # direita
    vx = x
    vy = y + 1
    if (valida(vx,vy)):
        cover = copy.deepcopy(s)
        t = cover[vx][vy]
        cover[vx][vy] = cover[x][y]
        cover[x][y] = t
        r.append(cover)

    return r

def h2(start,goal):
    dist = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    if (goal[i][j] == start[k][l]):
                        dist += abs(int(i-k)) +abs(int(j-l))

    return dist

# Função de conversão para str
def son2str(s):
    s1 = s[0] + s[1] + s[2]
    return ''.join([str(v) for v in s1])

def busca_a_star(start, goal, heuristica):
    h = []
    heappush(h,(heuristica(start, goal), start))
    pais = dict()
    visited = [start]
    jogada = 0

    while (len(h) > 0):
        jogada+=1
        print(jogada)
        (_, pai) = heappop(h)
        for filho in sons(pai):
            if filho not in visited:
                visited.append(filho)
                pais[son2str(filho)] = pai
                no = filho
                res = []
                profund = 0
                while no != start:
                    res.append(no)
                    no = pais[son2str(no)]
                    profund += 1
                res.append(start)
                res.reverse()
                if filho == goal:
                    print(len(visited))
                    return res
                else:
                    heappush(h, (heuristica(filho, goal)+ profund, filho))
    print("Nao tem solucao")

start = [[1,2,3],[4,0,5],[6,7,8]]
goal = [[1,2,3],[4,5,6],[7,8,0]]

busca_a_star(start, goal, h2)