# Crie um dicionário para armazenar nomes e telefones. Permita que o usuário:
# Adicion/e novos contatos
# Consulte pelo nome
# Exclua um contato
dic = {}


def adicionar_contato(nome, tel):
    dic[nome] = tel
    print(nome)

nome = input('nome: ')
tel = input('tel: ')

adicionar_contato(nome,tel)
print(dic)

def consultaNome():
    nomeBusca =input('nome busca')
    print('nome busca: ', nomeBusca)
    if nomeBusca in dic:
        print('nome encontrado', {dic[nomeBusca]})
    else:
        print('nome nao encontrado')
    return nomeBusca
        
print(consultaNome())

def excluirContato():
    nomeExcluir = input('nome exlcuir ')
    if nomeExcluir in dic:
        del dic[nomeExcluir]
    else:
        print('nao encontrado')
    return nomeExcluir
    
print(excluirContato())
print(dic)


frase = input('frase:')

divisao = frase.split()
for i in divisao:
    print(len(divisao))

print('divisao: ', divisao)

 
