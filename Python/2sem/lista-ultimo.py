livros = [
    'a casa ',
    'a rua ',
    'a lua ',
]

while True:
    pergunta = input('Quer adicionar digite a quer excluir digite e   ')
    if pergunta == 'a':
        adicao = input('adicionar:')
        livros.append(adicao)
        print(livros, 'posição:',len(livros))

    else:
        livros.pop() #ELIMINA ultimo adicionado 
        print(livros)

