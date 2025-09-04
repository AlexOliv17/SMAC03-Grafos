def insereArestaLista(listaAdj, vi, vj):
    lista_vi = listaAdj[vi]
    lista_vj = listaAdj[vj]

    simetrico = verificaSimetria(listaAdj)

    if simetrico:
        lista_vi.append(vj)
        lista_vj.append(vi)
    else:
        lista_vi.append(vj)

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

insereArestaLista({0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]}, 0, 2)