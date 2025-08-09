demandas = []

while True:
    pergunta = input('Quer adicionar digite a quer executar digite e')
    if pergunta == 'a':
        atividade = input('Atividade:')
        demandas.append(atividade)
        print(demandas, 'posição:',len(demandas))

    else:
        print(demandas)
