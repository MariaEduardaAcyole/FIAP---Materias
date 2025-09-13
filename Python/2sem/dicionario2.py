#DICIONARIOS
# Elemento : valor
# chave : conteudo
# nao tem ordem no dicionario (por exemplo: primeiro, segundo)
pessoa = {
    'nome':'helder',
    'idade':10,
    'peso': 83.10,
    'trabalho': {1: 'Fiap', 2:'itau', 3:'uber', 4:'segurança'}
}

if 'nome' in pessoa:
    print(pessoa['nome'])
else:
    print('chave nao encontrada')

print(pessoa)
rem = pessoa.pop('nome')
del pessoa['peso']
print(pessoa,rem)

pessoa.popitem()
print(pessoa)

pessoa2 = {
    'nome': 'duda',
    'trabalho': 'iau',
    'altura': 1.55
}
print(pessoa)
pessoa.update(pessoa2)
print(pessoa)

a = list(pessoa.keys())
print(a)
for i in pessoa.keys():
    print(i)

b = list(pessoa.values())
print(b)
for i in pessoa.values():
    print(i)

for i in pessoa.items():
    print(i[0], i[1])
    
