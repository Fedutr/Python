from datetime import date
ano_atual = date.today().year
contador_maior = 0
contador_menor = 0
for i in range(7):
    n = int(input('Digite o ano de nascimento: '))
    idade = ano_atual - n
    if idade >= 21:
        contador_maior += 1
    else:
        contador_menor += 1
print('O ano atual é {}, para atingir a maioridade, tem que ter nascido até o ano {}'.format(ano_atual, ano_atual-21))
print('{} pessoas ainda não atingiram a maioridade'.format(contador_menor))
print('{} pessoas atingiram a maioridade'.format(contador_maior))
