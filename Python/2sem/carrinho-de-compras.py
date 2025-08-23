car = []

def adicionar(produto):
    car.append(produto)
    print(produto, 'foi adicionado')

def remover(produto):
    # for i in car: = pelo elemento
    # foi i in range(len.(car)) = para percorrer pelo indice
    for i in range (len(produto)):
        if produto == car[i]:
            car.pop(i)
            break #para remover apenas uma unidade do item
def ver():
    for i in car:
        print(i)

while True:
    op = input('digete 1 pra adicionar')
    if op == '1':
        produto = input('digite onome:')
        adicionar(produto)
    elif op =='2':
        produto = input('nome do produto')
        remover(produto)
    elif op == '3':     
        ver()
    else:
        print('saindo')   
