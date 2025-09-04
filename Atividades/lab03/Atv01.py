def criaListaAdjacencias(matriz):
    dicionario = {}
    for i, linha in enumerate(matriz):
        dicionario[i] = []
        for j, valor in enumerate(linha):
            if valor > 0:
                dicionario[i].extend([j] * valor)
    print (dicionario)