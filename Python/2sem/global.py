def f1(a):
    print(a+x)

def f3(a):
    global x # tem que declarar que é global
    x = x+1
    print(a+x)

x = 4
f1(3)
f3(3)
print(x)