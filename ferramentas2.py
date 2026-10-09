# Primeira versão menos adequada

alunos = ["Ana","Hugo", "Paula", "Mariana", "Pedro", "Ana Paula"]

aluno_procurado = input("Digite o nome do aluno que você procura: ")

for item in alunos:
    if aluno_procurado.lower() in item.lower():
        print(item)

# Segunda versão mais adequada

alunos = ["Ana","Hugo", "Paula", "Mariana", "Pedro", "Ana Paula"]

aluno_procurado = input("Digite o nome do aluno que você procura: ")

alunos_encontrados = []
for item.lower() in alunos.lower():
    alunos_encontrados.append(item)
print(alunos_encontrados)