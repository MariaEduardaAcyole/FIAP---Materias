lista = [3,5,1,20,13]
chave = 12
def Busca (lista, chave):
    res = -1
    for i in range(len(lista)):
        if chave == lista[i]:
            res = i
            print('esta na lista index', i)

    return res

print(Busca(lista, chave))
