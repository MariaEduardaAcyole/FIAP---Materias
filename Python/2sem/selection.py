# Ordenação usando selection menor
#Selection Sort: percorre a lista procurando o menor elemento e o coloca na posição correta, repetindo isso para cada posição da lista.

l = [12, 68, 95, 41, 10, 71]
indice  = 0

def index_min(l, indice):
    menor = indice # menor = 0
    for i in range(indice,len(l)): #percorrer lista do index 0 ate o fim
        if l[menor] > l[i]:
            menor = i #troca o menor
    return menor

print(l)
for i in range (len(l)-1):
    min = index_min(l,i)
    aux = l[min]
    l[min] = l[i]
    l[i] = aux
    print(l)
