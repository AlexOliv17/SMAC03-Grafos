def criaDicionario(matriz):
    dicionario = {}
    for i, linha in enumerate(matriz):
        dicionario[i] = []
        for j, valor in enumerate(linha):
            if valor > 0:
                dicionario[i].append(j)
    #return dicionario
    print (dicionario)
