print('{}VELOCIDADE DA VIA - 80KM/H{}'.format('-'*5,'-'*5))
vel = float(input('Digite a velocidade do seu carro em km/h: '))
if vel > 80:
    ex = vel-80
    print('Você estava a {:.1f}km/h \nVocê terá de pagar uma multa de R${:.2f}'.format(vel,ex*7))
else:
    print('Você passou a {:.1f}km/h\nDentro do limite de velocidade'.format(vel))