# Importa a biblioteca matplotlib, que serve pra desenhar gráficos.
import matplotlib.pyplot as plt

# a) Faça o gráfico da função y = x (faça com 1000 pontos entre -100 e 100)
# b) Faça o gráfico da função y = x² (faça com 1000 pontos entre -100 e 100)

#range(-100, 101) → cria os números de -100 até 100.
x = [i for i in range(-100, 101)]
y = [i for i in range(-100, 101)]

#x e y são listas com os mesmos valores → então a linha será uma reta diagonal (porque y = x)

#plt.plot(x, y) → desenha o gráfico ligando os pontos (x, y).
plt.plot(x, y)

#plt.show() → mostra o gráfico.
plt.show()

#isso é uma função linear.

# GRAFICO DE Y = X²
x = [i for i in range(-100, 101)]
y = [i**2 for i in range(-100, 101)]
plt.plot(x,y, marker='o', linestyle='--')
plt.show()

# Isso gera uma curva em forma de U (parábola).
# isso é uma função quadrática.

plt.title('Título do gráfico')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.grid(True)
plt.show()


# Faça um degrade com as cores rgb na vertical e horizontal
#Cada linha é uma "faixa" de pixels
matriz_rgb = [
	[[0, 0, 0], [127, 127, 127], [0, 0, 0]],
	[[255, 255, 255], [0, 0, 0], [255, 255, 255]],
	[[0, 0, 0], [255, 255, 255], [0, 0, 0]]
                 ]

#Quadradinhos pretos e brancos alternados — tipo um tabuleiro de xadrez.
plt.imshow(matriz_rgb)
plt.show()

matiz_rgb2 = []
for j in range(256):
    matriz_rgb_linha = []
    for i in range(256):
        matriz_rgb_linha.append([j+i - (i+j)//256*255,j+i - (i+j)//256*255,j+i - (i+j)//256*255])
    print(matriz_rgb_linha)
    matiz_rgb2.append(matriz_rgb_linha)
print(matiz_rgb2)
plt.imshow(matiz_rgb2)
plt.axis('off')

plt.show()

# Pilotando o gráfico
# marker='o' para usar círculos, linestyle='-' para usar uma linha sólida
#plt.plot(x, y, marker='o', linestyle='-')
#plt.title('Gráfico de Coordenadas x, y')
#plt.xlabel('Eixo x')
#plt.ylabel('Eixo y')
#plt.grid(True) # Adiciona uma grade ao gráfico
#plt.show()

palavras = ['casa', 'carro', 'bicicleta', 'carro','carro','bicicleta']

for i in range(len(palavras)):
    print(i)
