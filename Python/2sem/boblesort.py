# Ordenação usando Bubble Sort menor para o maior
#Bubble Sort: compara pares de elementos vizinhos e os troca de lugar se estiverem fora de ordem, repetindo o processo até que a lista esteja ordenada.
l = [12, 68, 95, 41, 25, 71]

print("Antes da ordenação:", l)

h = len(l)

for iteracao in range(h - 1, 0, -1):
    for i in range(iteracao):
        if l[i] > l[i + 1]:
            # Troca os elementos
            aux = l[i]
            l[i] = l[i + 1]
            l[i + 1] = aux
    print("Após iteração:", l)

print("Depois da ordenação menor para o maior:", l)

# Ordenação usando Bubble Sort maior para o menor
for iteracao in range(h - 1, 0, -1):
    for i in range(iteracao):
        if l[i] < l[i + 1]:
            # Troca os elementos
            aux = l[i]
            l[i] = l[i + 1]
            l[i + 1] = aux
    print("Após iteração:", l)

print("Depois da ordenação maior para o menor:", l)

#
indice = 2

print("Antes da ordenacao com indice:", l)

def listar(indice):
    for iteracao in range(indice, 0, -1):
        for i in range(iteracao):
            if l[i] > l[i + 1]:
                # Troca os elementos
                aux = l[i]
                l[i] = l[i + 1]
                l[i + 1] = aux
        print("Após iteração com indice:", l)

print(listar(indice))
print("Depois da ordenação com indice:", l)


