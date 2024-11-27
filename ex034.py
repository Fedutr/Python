sal = float(input('Qual o salário do funcionário? R$'))
if sal > 1250:
    print('Você recebeu um aumento de 10%, seu novo salário é R${:.2f}'.format(sal*1.1))
else:
    print('Você recebeu um aumento de 15%, seu novo salário é R${:.2f}'.format(sal*1.15))