# Parte 1 - Contagem de 0 a 10
i = 0 
while i <= 10:
    print(i)
    i += 1

print('fim!')

# Parte 2 - Contagem de 50 a 60
b = 50
while b <= 60:
    print(b)
    b += 1

print('fim!')

# Parte 3 - Contagem regressiva de 10 a 1
c = 10
while c >= 1:
    print(c)
    c -= 1

print('feliz ano novo!')

# Parte 4 - Contagem até o número digitado
entrada = int(input('o digitado:'))
d = 1
while d <= entrada:
    print(d)
    d += 1

print('fim!')

# Parte 5 - Imprimir números pares até o valor digitado
dig = int(input('o digitado:'))
x = 0
while x <= dig:
    if x % 2 == 0:
        print(x)
    x += 1

# Parte 6 - Soma de números de 1 até um valor fornecido
fimIntervalo = int(input('o fim:'))
inicio = 1
soma = 0
while inicio <= fimIntervalo:
    soma += inicio
    inicio += 1
print(soma)

# Parte 7 - Média dos números de 1 até o valor fornecido
fimIntervalo = int(input('o fim:'))
inicio = 1
soma = 0
quantidade = 0

if fimIntervalo > 0:  # Verifica se o intervalo é válido
    while inicio <= fimIntervalo:
        soma += inicio
        quantidade += 1
        inicio += 1

    print("Média de 1 a", fimIntervalo, "=", soma / quantidade)
else:
    print("Intervalo inválido")

# Parte 8 - Interrupção com 'break' se o usuário digitar 0
prog = int(input('o entrada:'))
while prog <= 5:
    if prog == 0:
        break
    print(prog)  # Colocado fora da condição 'if'
    prog = int(input('o entrada:'))
