print('{}Calculador de Passagem{}'.format('='*6,'='*6))
d = float(input('Qual a distância da sua viagem: '))

# Forma de Condição Composta
'''if d > 200:
    print('Viajando {}km, sua passagem vai custar R${}'.format(d,d*0.45))
else:
    print('Viajando somente {}km, sua passagem vai custar R${}'.format(d,d*0.5))'''
# Forma de Condição Simplificada
print('Sua viagem será de {}km'.format(d))
# print('Você pagará R${:.2f}'.format(d*0.45) if d > 200 else 'Você pagará R${:.2f}'.format(d*0.50))
preço = d * 0.45 if d > 200 else d * 0.5
print('E o preço da sua passagem será de R${}'.format(preço))