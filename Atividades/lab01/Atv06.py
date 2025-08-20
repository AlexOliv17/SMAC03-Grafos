def contaRegressivaRecursao(numero):
    if numero > 0:
        print(numero)
        contaRegressivaRecursao(numero - 1)
        

contaRegressivaRecursao(10)