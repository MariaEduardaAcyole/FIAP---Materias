def parImpar(num):
    if num % 2 == 0:
        print('par')
    else:
        print('impar')    
    return num


while True:
    op = input('qual a opção (1) continuar parar (2)')
    if op == '1':
        num = float(input('QUal o numero'))
        parImpar(num)
    else:
        print('fim')
    


