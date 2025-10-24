#Uma função recursiva em Python é aquela que chama a si mesma para resolver um problema
def soma (l):
    if len(l) == 1:
        return l[0]
    return  l[0] + soma(l[1:])
l = [1,3,5,7]
print(soma(l))

#wile
i = 1
num = 3
multi = 1

while i <= num:
    multi = multi * i
    i += 1
print(multi)

#reursao
m = 1
f = 1

def fat(n):
    multi = 1
    while n > 0:
        multi *= n
        n = n -1
    return multi

def fat1(n):
    if n == 0:
        return 1
    return n * fat1(n-1)

print(fat1(3))

