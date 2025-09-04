import Atv02

def calcDensidadeLista(listaAdj):
    tipo = Atv02.tipoGrafoLista(listaAdj)
    tipo = 0 
    if tipo == 0 or 20 or 30:
        V = len(listaAdj.keys())
        E = calculaNumVetice(listaAdj, tipo)
        
        densidade = round((2*E)/(V*(V-1)),3) 
        print(densidade)
    else:
        V = len(listaAdj.keys())
        E = calculaNumVetice(listaAdj, tipo)

        densidade = round((E)/ (V * (V - 1)),3)
        print(densidade)


def calculaNumVetice(listAdj, tipo):
    E = 0
    for valores in listAdj.values():
        E += len(valores)

    if tipo in (0, 20, 30): 
        return E // 2 
    else:
        return E 
