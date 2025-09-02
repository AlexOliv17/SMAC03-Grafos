def verificaAdjacencia(matriz, vi, vj):    
    if (matriz[vi][vj] != 0):
        return print(True)
    else:
        return print(False)
    

verificaAdjacencia([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]], 0,3)