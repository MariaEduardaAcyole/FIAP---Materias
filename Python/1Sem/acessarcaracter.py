a = 'hoje tem aula'
quantidade = len(a)
print(quantidade) # 13
print('-'*5) # -----
print(a[3]) # e
print(a[5:8]) #tem
print(a[:]) # aparece tudo
print(a[len(a)-1]) # aparece o ultimo caractere
print(a[1:12:2]) # é de quanto em quanto


#numero de letras do nome e primeira letra
nome = 'duda'
quant = len(nome)
print(quant) # quantidade de letras do nome
print(nome[0]) #primeira letra

#  retorne uma palava invertida
print(nome[-1]+nome[-2]+nome[-3]+nome[-4])
print(nome[::-1]) #tras para frente
print(nome[::1]) # frente para tras

# peça o cpf e retorne se é valido ou nao se for retone a regia oque ele iro u o cpf

cpf = "1453822062"  # exemplo de CPF como string

soma = int(cpf[0]*10+ cpf[1]*9 + cpf[2]*8 + cpf[3]*7 + cpf[4]*6 + cpf[5]*5 + cpf[6]*4 + cpf[7]*3 + cpf[8]*2)

if 11 - soma % 11 >= 10:
    d1 = 0
else:
    d1 = 11 - soma % 11

print(d1)

soma = int(cpf[0]*11+ cpf[1]*10 + cpf[2]*9 + cpf[3]*8 + cpf[4]*7 + cpf[5]*6 + cpf[6]*5 + cpf[7]*4 + cpf[8]*3 + cpf[8]*2 )

if 11 - soma % 11 >= 10:
    d2 = 0
else:
    d2 = 11 - soma % 11

if d1 == cpf[-2] and d2 == cp[-1]:
    print(f'cpf invalido {d1} {d2}')
else: 
    print(f'cpf invalido {d1} {d2}')

