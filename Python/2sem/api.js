# 1. importe e biblioteca requests
import requests

# declare a url
url = 'https://viacep.com.br/ws/02851000/json/'
# pegue o cep e adicione na rota

cep = input('CEP: ')
cepDado = f'https://viacep.com.br/ws/{cep}/json/'
print(cepDado)

resultadoRequisicao = requests.get(url)
transformaEmDicionario = resultadoRequisicao.json()


def verCidade():
    cidade = transformaEmDicionario['localidade']
    return cidade

def verBairro ():
    bairro = transformaEmDicionario['bairro']
    return bairro

def verRua ():
    rua = transformaEmDicionario['logradouro']
    return rua

print(verCidade())
print(verBairro())
print(verRua())

print(verCidade())
