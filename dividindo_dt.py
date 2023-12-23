import pandas as pd

url = r'c:\Users\Willer\Desktop\dividindo_dados.csv'

df = pd.read_csv(url, sep=',', encoding='windows-1252')

df_parte_01 = df.iloc[:50, :]
df_parte_02 = df.iloc[50:, :]


try:
    df_parte_01.to_csv('divisao_01.csv', index=False)
    print("Download realizado com sucesso")
except:
    print("Falha no Download")



