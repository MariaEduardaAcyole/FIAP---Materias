l = []
for i in range (10):
    if i % 2 == 0:
        l.append(i)
print(l)

l1 = [2*i for i in range(10)]
print(l1)

notas = [7,2,9,8,4]
l2 = [i for i in notas if i >= 6]
print(l2)
