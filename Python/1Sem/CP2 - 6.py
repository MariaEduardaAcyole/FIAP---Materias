frase = input('Digite uma frase ou palavra:')

i = 0
frase2 = ''
while i < len(frase):
    if frase[i]!=' ' and frase[i]!='-' and frase[i]!=',' and frase[i]!='.':
        frase2 += frase[i]
    i += 1
if frase2 == frase2[::-1]:
    print(f'{frase} é um palíndromo!')