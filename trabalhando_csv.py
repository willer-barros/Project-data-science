import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas/main/superstore_data.csv'

dados = pd.read_csv(url, usecols=[0, 1, 6])
#o parametro usecols pode ser preenchido com os nomes das colunas ou seus indices



print(dados.head(10))