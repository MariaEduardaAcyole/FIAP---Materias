def depositar(valor):
    global saldo
    saldo = saldo + valor
    trans.append(valor)

def sacar(valor):
    global saldo
    saldo = saldo - valor
    trans.append(-valor)

def extrato():
    for i in trans:
        if i > 0:
            print(f'Deposito de R${i:.2f}')
        else:
            print(f'Saque de R${i:.2f}')
    print(f'Saldo final: {saldo:.2f}')

saldo = float(input('Qual o seu saldo: '))
trans = []
while True:
    op = input('Digite o que vc deseja: (1) saque; (2) deposito; (3) extrato; (4) sair: ')
    if op == '1':
        valor = float(input('Digite o valor do saque: '))
        sacar(valor)
    elif op == '2':
        valor = float(input('Digite o valor do deposito: '))
        depositar(valor)
    elif op == '3':
        extrato()
    elif op == '4':
        extrato()
        break
    else:
        print('Opção invalida!')
    print()
    print()