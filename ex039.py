from datetime import date
ano = int(input('Qual o ano que você nasceu: '))
anoatual = date.today().year
if anoatual - ano < 18:
    print('Não precisa se alistar ao serviço militar por enquanto')
    print('Você deve se alistar em {} ano(s)'.format(18-(anoatual-ano)))
elif anoatual - ano == 18:
    print('É a hora de se alistar')
else:
    print('Passou do tempo do alistamento')
    print('Já passou {} ano(s) do seu'
          ''
          ' alistamento obrigatório'.format((anoatual-ano)-18))