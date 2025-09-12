# Ex1

def f(x):
    if x <= -2:
        return x**2 + 3*x - 4
    elif x < 0:
        return 2*x + 5
    elif x < 4:
        return x**(1/2)
    elif x < 6:
        return x**3 - 3*x**2 - 10*x
    elif x < 8:
        return x**2 - 4*x - 20
    else:
        return 10

# Ex2

def le_matriz(l, c):
    m = []
    for j in range(l):
        linha = []
        for i in range(c):
            linha.append(int(input('digite um valor: ')))
        m.append(linha)
    return m

#Exercicio 3
def tam(m):
    return len(m), len(m[0])

m = [
    [1,2],
    [3,4]
]
print(tam(m))



#Ex4

def sub(a, b):
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        m = []
        for i in range(len(a)):
            linha = []
            for j in range(len(a[0])):
                linha.append(a[i][j] - b[i][j])
            m.append(linha)
        return m
    else:
        return None

#Exercicio 5
# a
desc = lambda x: x*0.9

# b
precos = [10.0, 23.5, 7.99, 100.0]
prec1 = [desc(i) for i in precos]

# c
prec2 = [desc(i) for i in precos if desc(i) > 20]
prec2 = [i for i in prec1 if i > 20]

#Exercicio 6
