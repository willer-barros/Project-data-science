import pandas as pd

data = [
     {"id": 1, "nome": "Alice", "idade": 25, "telefones": {"residencial": "123-456-7890", "celular": "987-654-3210"}},
    {"id": 2, "nome": "Bob", "idade": 30, "telefones": {"residencial": "111-222-3333", "celular": "444-555-6666"}},
    {"id": 3, "nome": "Charlie", "idade": 35, "telefones": {"residencial": "999-888-7777", "celular": "666-777-8888"}},
    {"id": 4, "nome": "David", "idade": 40, "telefones": {"residencial": "333-444-5555", "celular": "222-111-0000"}},
    {"id": 5, "nome": "Eva", "idade": 28, "telefones": {"residencial": "777-666-5555", "celular": "888-999-0000"}},
    {"id": 6, "nome": "Frank", "idade": 45, "telefones": {"residencial": "444-333-2222", "celular": "111-999-8888"}},
    {"id": 7, "nome": "Grace", "idade": 32, "telefones": {"residencial": "222-333-4444", "celular": "555-666-7777"}},
    {"id": 8, "nome": "Hank", "idade": 38, "telefones": {"residencial": "666-777-8888", "celular": "999-888-7777"}},
    {"id": 9, "nome": "Ivy", "idade": 27, "telefones": {"residencial": "888-999-0000", "celular": "777-666-5555"}},
    {"id": 10, "nome": "Jack", "idade": 33, "telefones": {"residencial": "555-444-3333", "celular": "000-111-2222"}}

]

df = pd.json_normalize(data)

print(df.head())
try:
    df.to_json('lendo_json.json')
    print("Download realizado com sucesso")
except:
    print("falha no download")

