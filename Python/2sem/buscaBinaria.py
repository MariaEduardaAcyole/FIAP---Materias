lista = [3,5,6,7,8] #lista ordenada
# dividir pela metade

# meio = int(len(lista)/2)
# print('index meio:',meio)

def Binario (lista, chave):
    inicio = 0
    fim = len(lista)-1
    while inicio <= fim:
        meio = (fim+inicio)//2
        if chave == lista[meio]:
            return meio
        elif chave > lista[meio]:
            inicio = meio+1
        elif chave < lista[meio]:
            fim = meio-1
    return -1
        
print(Binario(lista,8))
