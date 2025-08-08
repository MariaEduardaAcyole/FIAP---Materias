frase = input ('diite uma frase')
i = 0 
cont = 0
while i < len(frase):
    if frase[i]=='a' or frase[i]=='e' or frase[i]=='i' or frase[i]=='o' or frase[i]=='u':
        cont +=1
    i+=1
print(f'a frase tem {cont}') 
