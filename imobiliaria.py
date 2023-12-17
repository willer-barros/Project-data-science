import pandas as pd

url = r'c:\Users\Willer\Desktop\aluguel.csv'
dados = pd.read_csv(url, sep=';')

dados['Valor_mensal'] = dados['Valor'] + dados['Condominio']

dados['Valor_anual'] = dados['Valor_mensal'] * 12 + dados['IPTU']

dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro'] + ' com ' + \
                                        dados['Quartos'].astype('str') + ' quarto(s) ' + \
                                        ' e ' + dados['Vagas'].astype('str') + ' vaga(s) de garagem.'



print(dados.head())

