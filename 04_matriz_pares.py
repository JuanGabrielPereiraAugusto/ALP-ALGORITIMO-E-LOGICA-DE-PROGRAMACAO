# Rotinas: gera uma matriz de números pares e soma cada linha
def criar_matriz_pares(num_linhas, num_colunas):
    matriz = []
    numero = 2
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(numero)
            numero = numero + 2
        matriz.append(linha)
    return matriz


def somar_linhas(matriz):
    somas = []
    for linha in matriz:
        somas.append(sum(linha))
    return somas


matriz = criar_matriz_pares(3, 3)
for linha in matriz:
    print(linha)
print("Soma de cada linha:", somar_linhas(matriz))
