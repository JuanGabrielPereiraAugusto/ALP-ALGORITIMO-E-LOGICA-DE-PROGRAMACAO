# Vetores e registros: média mensal de compras de cada cliente
clientes = []

for i in range(3):
    nome = input("Nome do cliente: ")
    compras = []
    for mes in range(4):
        valor = float(input(f"Compra do mês {mes + 1}: "))
        compras.append(valor)
    clientes.append({"nome": nome, "compras": compras})

for cliente in clientes:
    media = sum(cliente["compras"]) / len(cliente["compras"])
    print(f'{cliente["nome"]}: média de R$ {media:.2f}')
