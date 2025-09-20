import requests
#viacep.com.br/ws/01001000/json/

url = 'https://viacep.com.br/ws/02851000/json/'

CEP = input('CEP: ')
urlDada = f'https://viacep.com.br/ws/{CEP}/json/'
print(urlDada)

resultado = requests.get(urlDada)
transformaEmDicionario = resultado.json()

# extrair as informações da API

def verCidade ():
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

#
