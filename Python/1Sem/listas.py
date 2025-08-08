# a = 10 
# b = a
# print('antes')
# print(a,b)
 
# print('depois')
# a = 20
# print(a,b)

a = [10,20,30]
# b = a
# b = a.copy 
b = a[:] #cria varivel nova, e não so aponta para a memoria 

print('antes')
print(a)
print(b)

print('depois')
a[0] = 27
print(a)
print(b)
