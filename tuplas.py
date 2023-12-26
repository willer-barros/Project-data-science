from random import randint

def gera_cod():
    return str(randint(0, 999))

estudantes = ['joao', 'maria', 'jose', 'tadeu']

codigo_estudantes = []

for i in range(len(estudantes)):
    codigo_estudantes.append((estudantes[i], estudantes[i][0] + gera_cod()))

print(codigo_estudantes)