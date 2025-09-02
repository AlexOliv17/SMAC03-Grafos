import numpy as np

def removeVertice(matriz, v):

    linhas = len(matriz)
    coluna = len(matriz[0])

    matriz = np.array(matriz)
    #print(matriz)

    for i in range(linhas):
        for j in range(coluna):
            if (i == v or j == v):
                matriz[ i, j] = -1
    print(matriz)

removeVertice([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]], 2)