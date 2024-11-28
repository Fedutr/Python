s = 0
cont = 0
for c in range(6):
    n1 = int(input('Digite o {}º número: '.format(c+1)))
    if n1 % 2 == 0:
        s += n1
        cont += 1
print('A soma dos {} números pares é igual a {}'.format(cont,s))