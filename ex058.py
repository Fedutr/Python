from random import randint
computador = randint (0,10)
print('-='*20)
print('Jogo de Adivinha')
print('-='*20)
# print(computador)

user = int(input('Digite um número: '))
contador = 1
while computador != user:
    contador += 1
    user = int(input('Digite um número: '))
print('''Você acertou!
O número que o computador pensou foi {}
Você demorou {} tentantivas para acertar'''.format(computador, contador))