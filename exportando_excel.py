import pandas as pd

url = r'c:\Users\Willer\Desktop\aluguel.csv'
dados = pd.read_csv(url, sep=';')

# Agrupe os dados pelo bairro e calcule a média de valores de aluguel
media_aluguel_por_bairro = dados.groupby('Bairro')['Valor'].mean()

# Ordene em ordem decrescente para identificar os bairros com as médias mais altas
bairros_mais_caros = media_aluguel_por_bairro.sort_values(ascending=False)

# Crie um DataFrame a partir da Série resultante
df_resultado = pd.DataFrame(bairros_mais_caros).reset_index()

# Exporte para um arquivo Excel
df_resultado.to_excel('media_aluguel_por_bairro.xlsx', index=False, engine='openpyxl')
