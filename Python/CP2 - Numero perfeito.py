while True:
    n = int(input('diite um numero para ser perfeito'))

    if n == 0 :
        break
    i = 1 
    soma = 0
   
    while i < n:
        if n%i == 0:
            soma += i
        i+= 1

    print(soma)

    if soma == n:
        print(f'{n}é um numero perfeito')
    else:
        print(f'{n}é um numero imperfeio')