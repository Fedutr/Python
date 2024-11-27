print('-='*20)
print('\033[1mCrédito de Financiamento\033[m')
print('-='*20)
valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
tempo = float(input('Deseja pagar em quantos anos? '))
prestacao = valor / (tempo * 12)
print('Financiamento o valor de R${:.2f} por {} anos, a prestação será de R${:.2f}'.format(valor, tempo, prestacao))
if prestacao > salario*0.3:
    print('A prestação compromete mais de 30% do seu salário\nNão conseguimos aprovar esse financiamento.')
else:
    print('Seu emprestimo foi \033[33mAPROVADO\033[m')
