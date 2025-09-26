# Ordenação usando Bubble Sort
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

print("Depois da ordenação:", l)
