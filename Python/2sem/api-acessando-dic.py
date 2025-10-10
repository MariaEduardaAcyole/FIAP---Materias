
dic = {'banana':'B', 'A': 'uva'}
for fruta in dic.values():
    print('fruta', fruta)

dic_a = {'nome': 'valor', 'nome2': 'valor2'}
dic_b = {'nome': 'valor', 'nome2': 'valorX'}
dic_a.update(dic_b)
print(dic_a)

import requests
url = 'https://viacep.com.br/ws/02851000/json/'
t = requests.get(url)
d = t.json()
print(d)

print(d['logradouro'][0])  # Primeira letra do logradouro
print(d['bairro'][0])      # Primeira letra do bairro

print('Logradouro:', d['logradouro'])
print('Bairro:', d['bairro'])

