turma = ("Joao", "Maria", "Osvaldo")
aluno_novo = input("Digite o nome do aluno: ")
try:
    alterando_turma = turma.append(aluno_novo)
    print("Aluno adicionado com sucesso!!")
except Exception as e:
    print('Esse aluno não esta cadastrado', e)

else:
    print(turma)