import matplotlib.pyplot as plt
# a) Faça o gráfico da função y = x (faça com 1000 pontos entre -100 e 100)
# b) Faça o gráfico da função y = x² (faça com 1000 pontos entre -100 e 100)
#x = [i for i in range(-100,101)]
##for i in range(-100,101):
##    x.append(i)
#y = [i**2 for i in range(-100,101)]
#plt.plot(x,y, marker='o', linestyle='--')
#plt.title('Título do gráfico')
#plt.xlabel('Eixo x')
#plt.ylabel('Eixo y')
#plt.grid(True)
#plt.show()
# faça de forma automática um código que o usuário entra com a qtde de linhas
# e colunas e vc faça um gráfico alternando as cores entre preto e branco
# assuma que a qtde de colunas é impar

# Faça um degrade com as cores rgb na vertical e horizontal
matriz_rgb = [
	[[0, 0, 0], [127, 127, 127], [0, 0, 0]],
	[[255, 255, 255], [0, 0, 0], [255, 255, 255]],
	[[0, 0, 0], [255, 255, 255], [0, 0, 0]]
                 ]

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


# Plotando o gráfico
# marker='o' para usar círculos, linestyle='-' para usar uma linha sólida
#plt.plot(x, y, marker='o', linestyle='-')
#plt.title('Gráfico de Coordenadas x, y')
#plt.xlabel('Eixo x')
#plt.ylabel('Eixo y')
#plt.grid(True) # Adiciona uma grade ao gráfico
#plt.show()
