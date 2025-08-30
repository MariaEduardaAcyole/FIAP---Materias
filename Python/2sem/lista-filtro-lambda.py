import math
angulos = [3,5.7,2*3, 4.5]

l3 = [math.cos(i) for i in angulos ] #a cada item da lista ele usa a função math faz o cosseno e adiciona na lista l3
print(l3)

umadez = [i for i in range(1,11)],
print(umadez)

pares = [i for i in range(1,21)if i % 2 ==0]
print(pares)

quadrado = [i **2 for i in range(10) ]
print(quadrado)

lista = ["python", "list"]
tamanhoPalavra = [len(i) for i in lista]
print(tamanhoPalavra)

frutas = ["maça","banana"]
tamanho = [i for i in frutas if len(i) > 4 ]
print(tamanho)

celsius = [0,10,5]
faren = [ i*9/5 + 32 for i in celsius ]
print(faren)

c = lambda  x: x*5/5+32
faren2 = [(c(i) for i in celsius)]
print(faren2)

# FILTRO
l6 = ['fizz' if i % 3 == 0 else i for i in range(1,21) ]
print(l6)
