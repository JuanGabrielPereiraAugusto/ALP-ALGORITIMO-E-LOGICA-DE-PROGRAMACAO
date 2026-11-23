# Repetição: soma todos os números de 1 até n (com validação da entrada)
n = int(input("Digite um número inteiro positivo: "))
while n <= 0:
    n = int(input("Valor inválido. Digite um número positivo: "))

contador = 1
soma = 0
while contador <= n:
    soma = soma + contador
    contador = contador + 1

print(f"A soma de 1 até {n} é {soma}")
