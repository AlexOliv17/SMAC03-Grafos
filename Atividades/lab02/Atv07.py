def removeAresta(matriz, vi, vj):
    matriz[vi][vj] = 0
    matriz[vj][vi] = 0

    print(matriz)

removeAresta([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]], 1, 0)