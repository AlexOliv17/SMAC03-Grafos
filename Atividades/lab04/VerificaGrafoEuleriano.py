import numpy as np

def caminhoEuleriano(matriz):
    matriz = np.array(matriz)
    n = len(matriz)
    
    total = 0
    vertice = 0

    while (total <= 2) and (vertice <= n):
        grau = verificaGrau(matriz, vertice)
        if verificaImpar(grau):
            total = total + 1
            vertice = vertice + 1
        else: 
            vertice = vertice + 1
    if total > 2:
        print(False)
    else:
        print(True)


def verificaGrau(matriz, vertice):
    linha = len(matriz)
    coluna = len(matriz[0])
    somatoria = 0

    for i in range(linha):
        for j in range(coluna):
            if i == vertice:
                somatoria += matriz[vertice][j]
    return somatoria

def verificaImpar(grau):
    if grau % 2 != 0:
        return True
    else:
        return False

caminhoEuleriano([[0, 1, 0, 0, 1, 0], [1, 0, 1, 1, 0, 1], [0, 1, 0, 1, 1, 1], [0, 1, 1, 0, 1, 1], [1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 1, 0]])