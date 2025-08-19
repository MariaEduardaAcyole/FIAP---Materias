#Calculo de PI

def soma(a=0, b=0, c=0):
    return a+b+c
a = soma(1,2)
print(a)

###############
l = [1,2]
a = soma(*l) # o mesmo que (l[0], l[1] ou [l0:2])
print(a)

################

def teste (*args): # args é padrão mas pode por outro nome
    print(args)

teste (1,2 'fasdas',4)

#############
def somar(*args): # args é o padrao mas pode por outro nome
    res = 0 
    for i in args:
        res+=i
    return res
a= somar(1,2,3,4)
print(a)

def printa (*args):
    textoJunto = ''
    for palavra in args:
        textoJunto += palavra + ''
        return textoJunto[:-1]
    
apresentarTexto = printa('duda', 'fafa')
print(apresentarTexto)


