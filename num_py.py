import numpy as np

url = 'https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv'

dados = np.loadtxt(url, delimiter=',', usecols=np.arange(1,87,1))
print(dados)