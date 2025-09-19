# 1
frutas = {
    'uva': 'roxo',
    'morango': 'vermelho',
    'laranja': 'laranja'
}
print(frutas)

#2 exibir valor
print(frutas['morango'])

#3 adicionar
frutas['kiwi'] = 'verde'
print(frutas)

#4 substituir valor
frutas['uva'] = 'verde'
print(frutas)

#5 remover
rem = frutas.pop('laranja')
print(rem)
print(frutas)

# acessar todas as chaves
for i in frutas.keys():
    print(i)

for j in frutas.values():
    print(j)

#
if 'uva' in frutas:
    print('a chave esta')
else:
    print('inexistent')
# oq for igual pega do segundo e adiciona o novo
frutas2 = {
    'maça': 'vermelho',
    'morango': 'verde',
}
frutas.update(frutas2)
print(frutas)

