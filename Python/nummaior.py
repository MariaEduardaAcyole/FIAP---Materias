num1 = float(input('numero 1: '))
num2 = float(input('numero 2: '))
num3 = float(input('numero 3: '))

if (num1>=num2) and (num1>=num3):
    maior = num1

elif (num2>=num1) and (num2>=num3):
    maior = num2

elif (num3>=num1) and (num3>=num1):
    maior = num3

######################

if (num1<=num2) and (num1<=num3):
    menor = num1

elif (num2<=num1) and (num2<=num3):
    menor = num2

elif (num3<=num1) and (num3<=num1):
    menor = num3


print('MAIOR',maior)
print('MENOR',menor)

print('nao foi')