# def quad(x):
#     res = x**2
#     return res
# a = quad(2)
# print(a)

# def cubo(c):
#     return c **3

# print(cubo(3))

def main():
    op = input('Digite se quer o q ou c:')
    d = int(input('Digite o número: '))
    if op == 'q':
        print(quad(d))
    elif op == 'c':
        print(cubo(d))
    else:
        print('Opção inválida!')

def quad(x):
    return x ** 2

def cubo(y):
    return y ** 3