fat = int(input('Digite um valor para calcular o fatorial:'))

# 5! = 5x4x3x2x1
# 5! = 1x2x3x4x5
i = 1
mult = 1
while i <= fat:
    mult = mult*i
    i += 1
print(f'O fatorial de {fat} é {mult}')