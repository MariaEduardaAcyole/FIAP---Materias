# correcao cp3 python

# frutaria 
print(f'{'-'*28}')
print(f'{'Código':6s} {'Fruta':8s} {'Preço/Kg(R$)':12s}')
print(f'{1:6d} {'Maçã':8s} {12.90:12.2f}')
print(f'{2:6d} {'Uva':8s} {9.30:12.2f}')
print(f'{3:6d} {'Banana':8s} {3.50:12.2f}')
print(f'{4:6d} {'Melancia':8s} {7.00:12.2f}')
print(f'{5:6d} {'Kiwi':8s} {37.50:12.2f}')
print(f'{'-'*28}')

valor = 0
while True:
    op = input('Escolha o código da fruta desejada ou 0 para sair:')
    if op == '0':
        break
    elif op == '1':
        tx = 12.90
    elif op == '2':
        tx = 9.30
    elif op == '3':
        tx = 3.5
    elif op == '4':
        tx = 7
    elif op == '5':
        tx = 37.50
    else:
        print('Código inválido')
    qtd = float(input('Digite a qtde (em kg):'))
    valor += qtd*tx

print(f'O valor total da sua compra é R${valor:.2f}')