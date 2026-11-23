# Arquivos: grava e lê o nome e a nota de cada aluno em um arquivo de texto
def gravar_notas(nome_arquivo, alunos):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for nome, nota in alunos:
            arquivo.write(f"{nome};{nota}\n")


def ler_notas(nome_arquivo):
    alunos = []
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, nota = linha.strip().split(";")
            alunos.append((nome, float(nota)))
    return alunos


gravar_notas("notas.txt", [("Ana", 8.5), ("Bruno", 5.0), ("Carla", 7.0)])
for nome, nota in ler_notas("notas.txt"):
    print(f"{nome}: {nota}")
