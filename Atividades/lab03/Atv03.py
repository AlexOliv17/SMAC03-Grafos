def removeArestaLista(listaAdj, vi,vj):
    lista_vi = listaAdj[vi]
    lista_vj = listaAdj[vj]

    simetrico = verificaSimetria(listaAdj)

    if simetrico:
        lista_vi.remove(vj)
        lista_vj.remove(vi)
    else:
        lista_vi.remove(vj)

    lista_vi.sort()
    lista_vj.sort()
    print(listaAdj)


def verificaSimetria(listaAdj):
    for chave,valores in listaAdj.items():
        for valor in valores:
            if chave not in listaAdj[valor]:
                return False
            else:
                return True