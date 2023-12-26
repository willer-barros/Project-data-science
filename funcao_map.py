#map

def dobra_nums(numero):
    return numero * 2

numeros = [1, 2, 3, 4, 5]
numeros_dobrados = map(dobra_nums, numeros)
numero_dobrados_lista = list(numeros_dobrados)

print(numero_dobrados_lista)