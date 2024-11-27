from datetime import date
nasc = int(input('Qual o ano que você nasceu: '))
atual = date.today().year
idade = atual - nasc
saldo = 18 - idade
if idade < 18:
    print('Quem nasceu no ano {} tem {} anos em {}'.format(nasc, idade, atual))
    print('Não precisa se alistar ao serviço militar por enquanto')
    print('Você deve se alistar em {}'.format(atual + saldo))
elif idade == 18:
    print('É a hora de se alistar')
elif idade > 18:
    print('Quem nasceu no ano {} tem {} anos em {}'.format(nasc, idade, atual))
    print('Passou do tempo do alistamento')
    print('Seu alistamento obrigatório foi em {}'.format((atual + saldo)))