import numpy as np

def insereVertice(matriz):
    linha_len = len(matriz)
    coluna_len = len(matriz[0])

    for i in range(linha_len):
        for j in range(coluna_len):
            if i == linha_len - 1 and j == coluna_len - 1:
                for linha in matriz:
                    linha.append(0)
                nova_linha = [0] * (coluna_len + 1)
                matriz.append(nova_linha)
    print(np.array(matriz))

insereVertice([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])