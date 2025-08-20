def dimensaoMatriz(matriz):
    numLinha = len(matriz)
    numColuna = len(matriz[0]) if matriz else 0
    diagonal = [matriz[i][i] for i in range(min(numLinha, numColuna))]
    return (numLinha, numColuna), diagonal