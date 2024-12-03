from random import randint
computador = randint (0,10)
print('-='*20)
print('Jogo de Adivinha')
print('-='*20)
# print(computador)
user = 100
contador = 0
while computador != user:
    contador += 1
    user = int(input('Digite um número: '))
    if user > computador:
        print('Menos... Tente mais uma vez.')
    else:
        print('Mais... Tente mais uma vez.')
print('''Você acertou!
O número que o computador pensou foi {}
Você demorou {} tentantivas para acertar'''.format(computador, contador))

# Meu código acima. DEU CERTO!

# # Código Guanabara NÃO DEU CERTO COMIGO
# from random import randint
# computador = randint(0,10)
# print('Sou seu computador... Acabei de pensar em um número entre 0 e 10')
# print('Será que você consegue adivinhar qual foi?')
# acertou = False
# palpites = 0
# while not acertou:
#      jogador = int(input('Qual é o palpite? '))
#      palpites += 1
#      if jogador == computador:
#          acertou == True
#      else:
#          if jogador < computador:
#              print('Mais... Tente mais uma vez.')
#          elif jogador > computador:
#              print('Menos... Tente mais uma vez.')
# print('Acertou com {} tentantivas. Parabéns!'.format(palpites))