
#Mostre o produto mais caro e o mais barato.

dic = {

}


while True:
    nome = input("Digite o nome do produto (ou 'fim' para parar): ")
    if nome.lower() == 'fim':
        break  # encerra o loop

    valor = float(input(f"Digite o preço de {nome}: R$ "))
    dic[nome] = valor  # adiciona ao dicionário

print(dic)


# Inicializa variáveis
preco_caro = 0
preco_barato = None
mais_caro = ''
mais_barato = ''

# Descobre o mais caro e o mais barato
for nome, valor in dic.items():
    if valor > preco_caro:
        preco_caro = valor
        mais_caro = nome

    if preco_barato is None or valor < preco_barato:
        preco_barato = valor
        mais_barato = valor

# Resultado final
print("\n💰 Produto mais caro:", mais_caro, f"– R$ {preco_caro:.2f}")
print("🪙 Produto mais barato:", mais_barato, f"– R$ {preco_barato:.2f}")
