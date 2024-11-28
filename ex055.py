# O jeito que fiz ficou melhor DEU CERTO!
'''maior = 0
menor = 1000

for p in range(5):
    peso = float(input('Diga o peso da pessoa {}: '.format(p+1)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O menor peso lido foi {:.1f}kg\nO maior peso lido foi {:.1f}kg'.format(menor, maior))'''

maior = 0
menor = 0

for p in range(5):
    peso = float(input('Diga o peso da {}ª pessoa: '.format(p+1)))
    if p == 0:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso lido foi {}kg'.format(maior))
print('O menor peso lido foi {}kg'.format(menor))