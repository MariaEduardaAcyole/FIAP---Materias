notas = [10,8,7]
nomes = ['aluno1:', 'aluno2:', 'aluno3']

sala = dict(zip(nomes,notas))
print(sala)


dic = {
    'nome':'duda',
    'idade':10,
}
#criar ou alterar um par chave valor
while True:
    op = input('1(adicionar) 2(consultar) 3(remover) 4(sair)')
    if op == '1':
        chave = input('chave: ')
        valor = input('valor: ')
        dic[chave] = valor
    elif op == '2':
        chave = input('digite a chave')
        print(dic.get(chave))
    elif op == '3':
        chave = input('digite:')
        if chave in dic:
            dic.pop(chave)
    elif op == '4':
        break
    else:
        print('invalido')
    print(dic)
        
print(dic)

#consultar valor de uma chave
if 'nome' in dic:
    print(dic['nome'])
else:
    print('chave nao encontrada')

#deletar uma chave
valor_del = input('qual deletar')

del dic[valor_del]
print(dic)
