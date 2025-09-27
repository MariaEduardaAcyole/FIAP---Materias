
# insertion sort
l = [12, 68, 95, 41, 10, 71]
print(l)
def insert_ord(l, i):
    aux = l[i]
    j = i - 1
    while j >= 0 and aux < l[j]:
        l[j+1] = l[j]
        j = j - 1
        print(l)
    l[j+1] = aux

for i in range(len(l)):
    insert_ord(l,i)



    l[i] = aux
    print(l)
