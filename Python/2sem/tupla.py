# tuplas

t = ('oi', 20, 3.56)
print(t)
prim = t[:-1]
print(prim)
print(t, type(t))

t1 = (1,2)
t2 = (3,4)
SOMA = t2+t1
print(SOMA)

nome, sobrenome = input("nome completo: ").split()
print(nome)
print(sobrenome)

a, b = (1,4)
print(a)
print(b)

# (index, valor)
l = ['oi', 10.4]
for i , j in enumerate(l):
    print(f'index: {i} | valor: {j}')

# list comprehension
# Adicionar elementos em uma tupla
def adTupla(t,elem):
    return t + tuple([elem])
a = (1,2,3)
print(adTupla(a, 5))

# INCOMPLETO Crie um maneira para remover elementos em uma tupla
def remtupla(t, elem):
    l = list(t)
    for i, j in enumerate(l):
        if elem == j:
            l.pop(i)
    return tuple(l)

# =========================
frutas = ('maçã', 'banana', 'uva', 'banana', 'laranja')

# primeiro e último
print('primeiro:', frutas[0])
print('último:', frutas[-1])

# Verifique se uma fruta digitada pelo usuário está na tupla
entrada = input('Digite o nome da fruta: ')

if entrada in frutas:
    print('Achei!')
else:
    print('Não achei!')

# Função para contar quantas vezes uma fruta aparece
def repete(frutas, nome):
    vezes = 0
    for i in frutas:
        if i == nome:
            vezes += 1
    return vezes

# Chama a função e mostra o resultado
print(f"A fruta '{entrada}' aparece {repete(frutas, entrada)} vez(es) na tupla.")

#================================
frutas = ('maçã', 'banana', 'uva', 'laranja')
print("Tupla original:", frutas)

# converte para lista
lista_frutas = list(frutas)

# remove o elemento desejado
lista_frutas.remove('banana')

# converte de volta para tupla
frutas = tuple(lista_frutas)
print("Tupla após remoção:", frutas)

