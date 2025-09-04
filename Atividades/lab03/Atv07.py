def removeVerticeLista(listaAdj, vi):
    del listaAdj[vi]
    for valores in listaAdj.values():
        while vi in valores:
            valores.remove(vi)
    print(listaAdj)