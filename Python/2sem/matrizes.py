#matriz: quando todas as listas tem o mesmo tamanho
from numpy.ma.core import append

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matriz)
print(matriz[2]) #7,8,9
a = matriz[0]
print(a[0]) # 1
print(matriz[0][1]) #1 (index [linha][coluna])

qtlinha = 3
qtcoluna = 4
matrizConstruida = []
for j in range (qtlinha):
    linha = []
    for i in range (qtcoluna):
        linha.append(input("digite "))
    matrizConstruida.append(linha)

print(matrizConstruida)

m = [
  [1,2,3],
  [4,5,6],
  [7,6,8]
]
qtdelinhasdamatriz= len(m)
qtdecolunasdamatriz= len(m[0])
print(qtdelinhasdamatriz)
print(qtdecolunasdamatriz)


################################################


a = [2,3,1]
b = a
print(a)
print(b)

a[0] = 5
print(a)
print(b)

cubo = [[[1,2,3],[4,5,6]], [[7,8,9], [5,3,1]]]
print(cubo[0][0][0])

===============================================
qtlinha = 5
qtcoluna = int((input("digite ")))

matrizConstruida = []
for j in range (qtlinha):
    linha = []
    for i in range (qtcoluna):
        linha.append(0)
    matrizConstruida.append(linha)
print(matrizConstruida)


