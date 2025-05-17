lista = [10,20,30,40]

for i in lista:
    print(i)
    if i == 20:
        break
    
#conta de 0 a 4
for i in range(5):
    print('A:',i)
    
#pula de 2 em 2 ate 10
for i in range(2,10,2):
    print('B: ',i)

#1)faça um programa para pintar os numeros de um inervalo digitado pelo usuario
#a = 3 b = 10 
# 2)faça com que mostre apenas os pares

a = int(input('a:'))
b = int(input('b:'))

for i in range(a,b+1):
    print('1)',i)

for c in range(a,b+1):
    if c%2 == 0 :
        print ('2-par)',c)

    
