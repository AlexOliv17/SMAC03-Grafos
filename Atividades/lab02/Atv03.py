import Atv01
import numpy as np

def calcDensidade(matriz):
    tipo = Atv01.tipoGrafo(matriz)
    densidade = 0
    E = contaArestas(matriz)
    V = contaVertice(matriz)
    if tipo == 0 or 20 or 30:
        densidade = round((2*E)/(V*(V-1)),3)
        print(densidade)
    else:
        densidade = round(E/(V*(V-1)),3)
        print(densidade)



def contaArestas(matriz):
    matriz = np.array(matriz)
    linha = len(matriz)
    coluna = len(matriz[0])
    contador = 0

    for i in range(linha):
        for j in range(coluna):
            contador = contador + matriz[i-1][j-1]
    return contador/2

def contaVertice(matriz):
    matriz = np.array(matriz)
    linha = len(matriz)
    coluna = len(matriz[0])

    if linha == coluna:
        return linha

calcDensidade([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])