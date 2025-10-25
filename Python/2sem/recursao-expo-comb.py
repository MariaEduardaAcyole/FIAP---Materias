
# potencia
# caso base =
# caso geral = a^n = a*a^n-1

def expo(a,p):
    if p == 0:
        return 1
    return  a * expo(a, p-1)

print("expo",expo(3,2))

# combinatoria
def comb(m,n):
    if  n == 0:
        return 1
    elif m == n:
        return 1
    elif m < n:
        return 0
    return comb(m-1,n)+ comb(m-1,n-1)
print(comb(10,5))



