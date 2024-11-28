contador = 0
soma = 0
idade_velho = 0
nome_velho = ()
mulher_nova = 0
print('-='*20)
for c in range(4):
    nome = str(input('Diga o seu nome: ')).strip()
    idade = int(input('Diga a sua idade: '))
    sexo = int(input('[ 1 ] Homem\n[ 2 ] Mulher\nQual é o seu sexo: '))
    print('-='*20)
    contador += 1
    soma += idade
    if sexo > 2:
        print('OPÇÃO INVALIDA')
        break
    if idade > idade_velho and sexo == 1:
        idade_velho = idade
        nome_velho = nome
    if sexo == 2 and idade < 20:
        mulher_nova += 1

media = soma / contador
print('A média de idade do grupo é de {:.1f} anos'.format(media))
print('O homem mais velho é o {} com {} anos de idade'.format(nome_velho, idade_velho))
print('{} mulheres tem menos de 20 anos'.format(mulher_nova))