from time import sleep
from random import choice
print('-='*6)
print('Jokenpô')
print('-='*6)

print('[ 1 ] Pedra')
print('[ 2 ] Papel')
print('[ 3 ] Tesoura')

escolha = int(input('Qual a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
e1 = str('Pedra')
e2 = str('Papel')
e3 = str('Tesoura')
lista = [e1, e2, e3]
maquina = choice(lista)

print('Eu escolho {}'.format(maquina))
if maquina == 'Pedra' and escolha == 3 or maquina == 'Papel' and escolha == 1 or maquina == 'Tesoura' and escolha == 2:
    print('\033[32mVENCI\033[m, \033[32mVENCI\033[m e \033[32mVENCI\033[m!!!')
elif maquina == 'Pedra' and escolha == 1 or maquina == 'Papel' and escolha == 2 or maquina == 'Tesoura' and escolha == 3:
    print('Empate, vamos outra?')
elif escolha > 3:
    print('Escolha errada!')
else:
    print('Poxa vida, perdi!')
