import pandas as pd
'''
df = pd.DataFrame({
    'Animal': ['cachorro', 'gato', 'elefante', 'cachorro', 'gato', 'elefante'],
    'Cor': ['preto', 'branco', 'cinza', 'marrom', 'preto', 'marrom'],
    'Quantidade': [2, 3, 1, 4, 2, 2]
})

result = df.groupby(['Animal', 'Cor'])['Quantidade'].sum().reset_index()
result_2 = df.groupby(["Animal"]).sum(numeric_only='True')



print(result_2)
'''

import pandas as pd

dados = pd.DataFrame([['Feira', 'Cebola', 2.5], 
                        ['Mercado', 'Cebola', 1.99], 
                        ['Supermercado', 'Cebola', 1.69], 
                        ['Feira', 'Tomate', 4], 
                        ['Mercado', 'Tomate', 3.29], 
                        ['Supermercado', 'Tomate', 2.99], 
                        ['Feira', 'Batata', 4.2], 
                        ['Mercado', 'Batata', 3.99], 
                        ['Supermercado', 'Batata', 3.69]],
                        columns = ['Local', 'Produto', 'Preço'])
print(dados)