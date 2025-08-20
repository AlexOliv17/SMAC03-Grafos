def valorCelula(matriz, i, j):
    num_linhas = len(matriz)
    num_colunas = len(matriz[0]) if matriz else 0

    if i < 0 or i >= num_linhas or j < 0 or j >= num_colunas:
        print("Erro")
    else:
        print(f"Celula[{i}][{j}] = {matriz[i][j]}")