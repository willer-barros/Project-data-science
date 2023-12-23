import pandas as pd

url = r'c:\Users\Willer\Desktop\dividindo_dados.csv'

df = pd.read_csv(url, sep=',', encoding='windows-1252')

print(df.shape)


