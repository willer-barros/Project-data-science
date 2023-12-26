'''
lista = [1, 2, 3, 4, 7]

print(len(lista))
print(max(lista))
print(min(lista))

---------------------------------------------------------------

nota_turma = ['joao', 8, 9, 10, 'lucas', 9,7,6, 'tadeu', 5, 6, 8, 'sergio', 6, 10, 9]

nomes = []
notas = []

for item in nota_turma:
    if isinstance(item, str):
        nomes.append(item)

    else:
        notas.append(item)

print('Nomes: ' ,nomes)
print('Notas: ' ,notas)
'''

nota_turma = ['joao', 8, 9, 10, 'lucas', 9,7,6, 'tadeu', 5, 6, 8, 'sergio', 6, 10, 9]

nomes = []

for i in range(len(nota_turma)):
    if isinstance(nota_turma[i], str):
        nomes.append(nota_turma[i])

print(nomes)