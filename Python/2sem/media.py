
def ler(n):
    l = []
    for i in range (n):
        l.append(float(input('Nota:')))
    return l     

def mostrar(notas):
    for i in notas:
        print(i)

def media(notas):
    soma = 0
    for i in notas:
        soma+=i
    return soma/len(notas)

mediafinal = media(ler(3))
print(mediafinal)