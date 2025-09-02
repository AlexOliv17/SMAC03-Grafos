import numpy as np

def tipoGrafo(matriz):
    tipo  = 0
    matriz = np.array(matriz)
    tipo = verificaDiagonal(matriz)
    tipo = verificaArestaParalela(matriz, tipo)
    tipo =  verificaAssimetria(matriz, tipo)
    return tipo

def verificaDiagonal(matriz):
    linha = len(matriz)
    coluna = len(matriz[0])
    diagonal = False
    for i in range(linha):
        for j in range(coluna):
            if i == j and matriz[i-1][j-1] != 0:
                diagonal = True
    if diagonal:
        return 30
    else:
        return 0
    
def verificaArestaParalela(matriz, tipo):
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in range(linha):
        for j in range(coluna):
            if matriz[i-1][j-1] >= 2:
                tipo = 20
    return tipo

def verificaAssimetria(matriz, tipo):
    linha = len(matriz)
    coluna = len(matriz[0])
    simetria = True
    for i in range(linha):
        for j in range(coluna):
            if matriz[0][0] != matriz[linha-1][coluna-1]:
                simetria = False
            elif matriz[i-1][j-1] != matriz[j-1][i-1]:
                simetria = False
    if tipo == 0 and not simetria:
        tipo = 1
    elif tipo == 20 and not simetria:
        tipo = 21
    elif tipo == 30 and not simetria:
        tipo = 31
    return tipo

tipoGrafo([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])