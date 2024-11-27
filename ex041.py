from datetime import date
nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade < 10:
    print('Categoria: MIRIM')
elif idade < 15:
    print('Categoria: INFANTIL')
elif idade < 20:
    print('Categoria: JUNIOR')
else:
    print('Categoria: MASTER')