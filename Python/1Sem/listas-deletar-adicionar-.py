lista = ['nome', 18, True, 2.99]
print(lista)

idt = ['dado1', 'dado2']
notas = [2.0, 5.5, 10, 6.1]

print(notas[1])
print(type(notas[1]))
print(notas[2:4])

i = 0
while i < len(notas):
    print(notas[i])
    i += 1

pala = list('fiap')
print(pala, len(pala))

animais = []
print(animais)

animais.append('joao')
print(animais)
animais.append('maria')
print(animais)

# animais.append(['vitor','gabriela']) #['joao', 'maria', ['vitor', 'gabriela']] ERRADO
# print(animais)

animais.extend(['vitor','gabriela']) 
print(animais)

# names = []
# while True:
#     n = input('nomes: ')

#     if n == 'sair':
#         print(names)
#         break
#     else:
#         names.append(n)
#         print(names)

nome = ['a','b','c']
print(nome)
nome.pop(1) #ELIMINA  se tiver vazio elimina o ultimo
print(nome)



fila = []
while True:
    p = input('opçao: ')

    if p == '1':
        g = input('gente')
        fila.append(g)
        print(fila)

    elif p == '2':
        fila.pop(0) #ELIMINA
        print(f'{g} foi removido')
        print(fila)

    else:
        print('saiu')
        print(fila)

