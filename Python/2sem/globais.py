# Vamos modificar a variável global diretamente usando global
a = [1, 2]  # variável global 'a'

def f5():
    global a  # Definimos que vamos modificar a variável global 'a'
    a = [3, 4]  # A variável 'a' será modificada aqui

# Chama a função para modificar 'a'
f5()
print(a)  # Agora 'a' foi alterada para [3, 4]

##########################

# A função funcaoComGlobal() modifica a variável global 'm'
def funcaoComGlobal():
    global m  # Variável global 'm'
    m = [10, 10]  # Agora 'm' será alterada para [10, 10]

# Inicializando 'a' e 'm' globalmente
a = [1, 2]
m = [1, 2]  # Antes da alteração

funcaoComGlobal()  # Chama a função para alterar 'm'

# Agora, 'a' não foi alterado, mas 'm' foi modificado
print(a)  # Vai imprimir [1, 2], pois 'a' não foi modificada
print(m)  # Vai imprimir [10, 10], pois 'm' foi alterada na função
