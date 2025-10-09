dicionario

# Crie um dicionário para armazenar nomes e telefones. Permita que o usuário:
# Adicion/e novos contatos
# Consulte pelo nome
# Exclua um contato
dic = {}
nome = input('nome: ')
tel = input('tel: ')

def adicionar_contato(nome):
    dic[nome] = tel
    print(nome)

adicionar_contato('duda')
print(dic)


def consultaNome():
    nomeBusca =input('nome busca')
    print('nome busca: ', nomeBusca)
    if nome == nomeBusca:
        print('nome encontrado')
    else:
        print('nome nao encontrado')
    return nomeBusca
        
print(consultaNome())

def excluirContato():
    nomeExcluir = input('nome exlcuir ')
    del dic[nome]
    return nomeExcluir
    
print(excluirContato())
print(dic)
