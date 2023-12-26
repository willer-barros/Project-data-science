# lambda
'''
somar_lambda = lambda nota: nota + 5

nota_aluno = int(input("Digite a nota do aluno: "))
nova_nota = somar_lambda(nota_aluno)
print(nova_nota)
'''

N1 = int(input("Digite a primeira nota: "))
N2 = int(input("Digite a secundaria nota: "))
N3 = int(input("Digite a terceira nota: "))

media_ponderada = lambda x, y, z: (x * 2 + y * 3 + z * 5) / 10
media_feita = media_ponderada(N1, N2, N3)

print(f"a nota do aluno: {media_feita}")


