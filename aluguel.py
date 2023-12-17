import pandas as pd

url = r'c:\Users\Willer\Desktop\aluguel.csv'
dados = pd.read_csv(url, sep=';')

selecao_1 = dados['Quartos'] ==1
dados[selecao_1]

selecao_2 = dados['Valor'] < 1200
dados[selecao_2]

selecao_final = (selecao_1) & (selecao_2)
dados[selecao_final]

print(dados[selecao_final])





'''
descobrindo_nulo = dados.isnull()
soma_nulo = dados.isnull().sum()
substituindo_nulos_por_zero = dados.fillna(0).isnull().sum()
imoveis_comerciais = ['Conjunto Comercial/Sala', 'Prédio Inteiro', 'Loja/Salão',
 'Galpão/Depósito/Armazém', 'Casa Comercial', 'Terreno Padrão',
 'Box/Garagem', 'Loja Shopping/ Ct Comercial',
 'Chácara' 'Loteamento/Condomínio' 'Sítio' 'Pousada/Chalé' 
 'Hotel' 'Indústria']

somente_declarados_lista = dados.query('@imoveis_comerciais in Tipo')
nao_declarados_lista = dados.query('@imoveis_comerciais not in Tipo')
'''
#df_resultado = pd.DataFrame(mais_alto).reset_index()
#media = dados.groupby('Tipo')['Quartos'].mean()
#unicos = dados['Bairro'].nunique()
#media_aluguel_mais_caro = dados.groupby('Bairro')['Valor'].mean()
#mais_alto = media_aluguel_mais_caro.sort_values(ascending=False)
#print(dados.Tipo.unique())
#media_aluguel = dados['Valor'].mean()

#media_tipo = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
#grafico = media_tipo.plot(kind='barh', figsize=(14, 10), color = 'red')

#ptl.show()
