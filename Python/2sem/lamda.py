soma = lambda x,y,z: x+y+z
b = soma(4,5,6)
print(b)

letra = lambda x: x.upperCase()
b = "duda acyole"
c = b[::-1]
print(c)

palavra = "ovo"

#palindromo = lambda palavra: palavra[::-1]
#palindromo = lambda palavra: palavra == palavra[::-1]
palindromo = lambda x: 'verdadeiro' if x == x[::-1] else 'falso'
c = palindromo(palavra)
print(c)

if palavra == palindromo(palavra):
    print('é palidromo')
else:
    print('nao é')
