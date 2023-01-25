from buscaEmProfundidade import *
from buscaEmLargura import *
from buscaGulosa import *
from aEstrela import *
import numpy as np

estadoFinal = [[1,2,3],[4,5,6],[7,8,0]]

entrada = (input('Digite a entrada:'))
entrada = list(map(int, entrada))
entrada = np.reshape(entrada, (3, 3)).tolist()
print('Entrada:', entrada)
estadoAtualBL, custoCaminhoBL, custoEspacoBL, custoTempoBL, profundidadeSolBL, profundidadeMaxBL = buscaEmLarguraMain(entrada, estadoFinal)
estadoAtualBP, custoCaminhoBP, custoEspacoBP, custoTempoBP, profundidadeSolBP, profundidadeMaxBP = buscaEmProfundidadeMain(entrada, estadoFinal)
estadoAtualBG, custoCaminhoBG, custoEspacoBG, custoTempoBG, profundidadeSolBG, profundidadeMaxBG = buscaGulosa(entrada, estadoFinal)
estadoAtualBA, custoCaminhoBA, custoEspacoBA, custoTempoBA, profundidadeSolBA, profundidadeMaxBA = buscaAEstrela(entrada, estadoFinal)

print('\n-----------------------------------------------')
print('Algoritmo: Busca em Largura\nSolução: {}\nCusto do Caminho: {}\nCusto do Espaço: {}\nCusto de tempo: {}\nProfundidade da Solução: {}\nProfundidade Máxima Atingida: {}\n'.format(estadoAtualBL, custoCaminhoBL, custoEspacoBL, custoTempoBL, profundidadeSolBL, profundidadeMaxBL))
print('Algoritmo: Busca em Profundidade\nSolução: {}\nCusto do Caminho: {}\nCusto do Espaço: {}\nCusto de tempo: {}\nProfundidade da Solução: {}\nProfundidade Máxima Atingida: {}\n'.format(estadoAtualBP, custoCaminhoBP, custoEspacoBP, custoTempoBP, profundidadeSolBP, profundidadeMaxBP))
print('Algoritmo: Busca Gulosa\nSolução: {}\nCusto do Caminho: {}\nCusto do Espaço: {}\nCusto de tempo: {}\nProfundidade da Solução: {}\nProfundidade Máxima Atingida: {}\n'.format(estadoAtualBG, custoCaminhoBG, custoEspacoBG, custoTempoBG, profundidadeSolBG, profundidadeMaxBG))
print('Algoritmo: Busca A*\nSolução: {}\nCusto do Caminho: {}\nCusto do Espaço: {}\nCusto de tempo: {}\nProfundidade da Solução: {}\nProfundidade Máxima Atingida: {}\n'.format(estadoAtualBA, custoCaminhoBA, custoEspacoBA, custoTempoBA, profundidadeSolBA, profundidadeMaxBA))