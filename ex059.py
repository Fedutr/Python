operação = 0
while operação != 5:
    v1 = float(input('Digite um valor: '))
    v2 = float(input('Digite outro valor: '))
    operação = int(input('''O que você quer fazer:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] novos números
    [ 5 ] Sair do programa
    '''))

    if operação == 1:
        print('A soma de {:.1f} com {:.1f} é igual a {:.1f}'.format(v1, v2, v1+v2))
        print('-'*20)
    elif operação == 2:
        print('A multiplicação de {:.1f} e {:.1f} é igual a {:.1f}'.format(v1, v2, v1*v2))
        print('-'*20)
    elif operação == 3:
        if v1 > v2:
            print('O Maior valor digitado foi {} e o menor {}'.format(v1, v2))
            print('-'*20)
        if v1 < v2:
            print('O maior valor digitado foi {} e o menor {}'.format(v2, v1))
            print('-'*20)
        else:
            print('O valores são iguais')
            print('-'*20)
    elif operação == 4:
        print('-'*20)
