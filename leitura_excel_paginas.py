import pandas as pd

url = 'https://github.com/alura-cursos/Pandas/blob/main/emissoes_CO2.xlsx?raw=True'

dados = pd.read_excel(url)
#emissoes_C02, emissoes_percapita, fontes

visualiza_paginas = pd.ExcelFile(url).sheet_names #visualiza as paginas dentro do arquivo
percapita = pd.read_excel(url, sheet_name='emissoes_percapita')# sheet_name escolhe a pagina que quer trabalhar
emissoes_co2 = pd.read_excel(url, sheet_name='emissoes_C02')
fontes = pd.read_excel(url, sheet_name='fontes')

intervalo = pd.read_excel(url, sheet_name='emissoes_C02', usecols="A:D", nrows=25)


print(intervalo)