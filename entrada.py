import numpy as np

entrada = list(input('Digite a matriz de entrada (9 digitos): '))
try:
    matriz = np.array(entrada).reshape(3,3)
except ValueError:
    while(len(entrada)!=9):
        entrada = list(input('Digite a matriz de entrada (9 digitos): '))
        matriz = np.array(entrada).reshape(3,3)

print(matriz)