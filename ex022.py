""" Minha solução (DEU CERTO)
nome = input('Digite o seu nome completo: ')
nome = nome.strip()

print('Seu nome todo em maiúsculo fica: {}'.format(nome.upper()))
print('Seu nome todo em minúsculo fica: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
dividido = nome.split()
print('Seu primeiro nome tem: {} caracteres'.format(len(dividido[0])))"""

"""Solução Guanabara"""
nome = str(input('Digite o seu nome completo:')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))