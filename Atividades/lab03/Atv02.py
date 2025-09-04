def tipoGrafoLista(listaAdj):
    tipo = 0
    tipo = verificaPseudografo(listaAdj)
    tipo = verificaMultigrafo(listaAdj, tipo)
    tipo = verificaSimetria(listaAdj, tipo)
    return tipo

def verificaPseudografo(listaAdj):
    for chave,valores in listaAdj.items():
        if chave in valores:
            return 30
    return 0 

def verificaMultigrafo(listaAdj, tipo):
    for valores in listaAdj.values():
        if len(valores) != len(set(valores)):
            tipo = 20
    return tipo

def verificaSimetria(listaAdj, tipo):
    for chave,valores in listaAdj.items():
        for valor in valores:
            if chave not in listaAdj[valor]:
                match tipo:
                    case 0:
                        tipo = 1
                    case 20:
                        tipo = 21
                    case 30:
                        tipo = 31
    return tipo