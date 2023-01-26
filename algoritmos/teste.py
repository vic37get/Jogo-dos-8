estadoInicial = [[1,2,3],[4,5,6],[7,0,8]]
estadoFinal = [[1,2,3],[4,5,6],[7,8,0]]

lista = []

lista.append((estadoInicial, 0))

lista.append((estadoFinal, 0))

estado, profundidade = lista.pop()

