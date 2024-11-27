''' Forma que eu resolvi. DEU CERTO
from random import randint
print('O computador vai pensar um número, será que você acerta qual foi?')
num = int(input('Digite um número de 0 a 5: '))
numpc = randint(0,5)
if num == numpc:
    print('Você deu sorte, acertou o número!')
else:
    print('Não foi dessa vez, o número que o computador pensou foi {}'.format(numpc))'''

# Forma do Guanabara
from random import randint
from time import sleep
computador = randint(0,5) #Faz o computador "PENSAR"
print('-=-'*20)
print('Vou pensar em um número emtre 0 e 5. Tente adivinhar....')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))