con = set ([9,6,8])

a =  {1,2,3}
b =  {2,4,5}
print(a)

#a.add(1)
#a.add(2)
#a.add(3)
#a.add(4)
print(a)

# CONJUNTOS

c = a - b
u = a | b
i = a & b
print('diferença', c)
print('uniao', u)
print('intersecção', i)

if 1 in a:
    print('esta no conjunto')
else:
    print('nao esta')

aa = set(a)
bb = set(b)

# valores comuns as duas listas
cc = aa & bb
c = list(cc)
print('valores comuns', c)

# Os valores que so existem na primeira
dd = aa - bb
d = list(dd)
print('valores so da primeira',d )

# so na segunda
ee = bb & aa
e = list(ee)
print(e)

# lista com os elementos nao repetidos
ff = (aa | bb) - (aa & bb)
f = list(ff)
print(f)

gg = aa^bb
g = list(gg)
print(g)
