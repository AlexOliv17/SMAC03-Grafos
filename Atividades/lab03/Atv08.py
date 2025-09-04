def verificaAdjacenciaLista(listaAdj, vi, vj):
    lista_vi = listaAdj[vi]
    lista_vj = listaAdj[vj]
    adjacencia = False

    for valor in lista_vi:
        if valor == vj:
            adjacencia = True
            break
    for valor in lista_vj:
        if valor == vi:
            adjacencia = True
            break
        else:
            adjacencia = False
    print(adjacencia)